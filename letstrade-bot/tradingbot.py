import alpaca_trade_api as api
import talib
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
import config
from datetime import datetime, date, timedelta
import pytz
import numpy as np
import schedule as sc
import time
import yfinance as yf
import sqlite3
import pandas_market_calendars as mcal
import datetime
import pytz
def recusrion():
    timeZ_Ny = pytz.timezone('America/New_York')
    UTC = pytz.utc

    connection = sqlite3.connect(config.DB_FILE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute("""
        SELECT symbol FROM watchlist
    """)

    rows = cursor.fetchall()
    symbols = []
    stock_dict = {}
    for row in rows:
        symbol = row['symbol']
        symbols.append(symbol)


    def trade():
        if rows:
            #get the current date 
            my_date = date.today()
            #when using the 200 sma it is nice to look further back
            last_week = my_date - timedelta(days = 7)
            diff = max(1, (my_date.weekday() + 6) % 7 - 3)
            #calculate yesterda as business day
            yes_bid = my_date - timedelta(days=diff)

            tradeing_client = api.REST(config.API_Key, config.API_Secret, config.URL_ENDPT)
            BASE_URL = config.URL_ENDPT
            x = 1
            #get active postions 
            x = 1
            tradeing_client = api.REST(config.API_Key, config.API_Secret, config.URL_ENDPT)
            orders = tradeing_client.list_positions()  
            order_symbols = [order.symbol for order in orders if x == 1]

            for symbol in symbols:
                if symbol not in order_symbols:
                    print(f"Symbol {symbol} does not have an active trade will look for trade to enter")
                    
                    #get price data from alpaca api
                    bars = yf.download(tickers = symbol,start=last_week, end=my_date, interval = '5m', rounding = True )
                    print(my_date)
                    bars.head()
                    # #put bars into np array
                    price = [bar for bar in bars['Close'] if bar != "NaN"]
                    prices = np.array(price)
                    open_bar = [bar for bar in bars['Open'] if bar != "NaN"]
                    opens = np.array(open_bar)
                    high_bar = [bar for bar in bars['High'] if bar != "NaN"]
                    highs = np.array(high_bar)
                    low_bar = [bar for bar in bars['Low'] if bar != "NaN"]
                    lows = np.array(low_bar)
                    volume_bar = [bar for bar in bars['Volume'] if bar != "NaN"]
                    volumes = np.array(volume_bar)
                    #define the TA-LIB tools that I want to use to base my strat around 
                    print("go here")
                    if len(prices) > 51:
                        RSI = talib.RSI(prices,14)
                        SMA_200 = talib.SMA(prices, timeperiod=200)
                        SMA_50 = talib.SMA(prices, timeperiod=50)
                    engulfing = talib.CDLENGULFING(opens, highs, lows, prices)
                    
                    # #Get the value of the most recent element in the np array.
                    length_sma_200 = (len(SMA_200))-1
                    current_SMA_200 = SMA_200[length_sma_200]
                    length_sma_50 = (len(SMA_50))-1
                    current_SMA_50 = SMA_50[length_sma_50]
                    length_RSI = (len(RSI))-1
                    current_RSI = RSI[length_RSI]
                    len_engulfing = (len(engulfing))-1
                    current_engulfing = engulfing[len_engulfing]
                    length_price = (len(prices))-1
                    current_price = prices[length_price]
                    #define params for taking profit and stoping
                    take_profit = round((current_price*.05)+current_price,2)
                    lost_profit = round(current_price-(current_price*.025),2)
                    #now that we have all the elements we need we can create the parameteres for the strat.
                    print(f"current stock {symbol}")
                    print(f"current Price: {current_price}")
                    print(f"current SMA 200: {current_SMA_200}")
                    print(f"current SMA 50: {current_SMA_50}")
                    print(f"current RSI 14: {current_RSI}")
                    print(f"Candle patter: {current_engulfing}")


                    #time to write the code that will conduct autotrading for me
                    if current_price > current_SMA_50 and current_price > current_SMA_200 and current_engulfing > 0:
                            print(f"Entering a Trade with stock {symbol} at price {current_price}")
                            tradeing_client.submit_order(
                                symbol=symbol,
                                side='buy',
                                type='market',
                                qty='1',
                                time_in_force='day',
                                order_class='bracket',
                                take_profit=dict(
                                    limit_price=take_profit,
                                ),
                                stop_loss=dict(
                                    stop_price=lost_profit,
                                    limit_price=lost_profit,
                                )
                            )   
        else:
            print("no stocks in watchlist")
                        
        

    sc.every(10).seconds.do(trade)

    #do program stuff to figure out if the stock market is open
    nyse = mcal.get_calendar('NYSE')
    my_date = date.today()
    exchange = (nyse.valid_days(start_date = my_date, end_date = my_date))
    while exchange.size > 0:
        dt_Ny = datetime.datetime.now(timeZ_Ny)
        e = dt_Ny#datetime.datetime.now()    
        current_time = (e.strftime("%I:%M:%S %p"))
        m1 = current_time

        m2 = datetime.datetime.strptime(m1, "%I:%M:%S %p").time()
        #type cast variable to a string becase I can compare a string variable and time variable
        m3 = str(m2)
        print(m3)
        
        if m3 < '16:30:00' and m3 > '09:30:00':
            print(current_time)
            sc.run_pending()
            time.sleep(290) 

        else:
            print("market currently not open")
            time.sleep(30) 
            
    else:
        print("market closed")
        time.sleep(30)
        recusrion()
        

recusrion()
print("code completed")