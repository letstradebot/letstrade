from re import X
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import config
from alpaca_trade_api.rest import TimeFrameUnit
from matplotlib import *
import yfinance as yf
import numpy as np
import backtrader as bt
from matplotlib.dates import (HOURS_PER_DAY, MIN_PER_HOUR, SEC_PER_MIN,
                              MONTHS_PER_YEAR, DAYS_PER_WEEK,
                              SEC_PER_HOUR, SEC_PER_DAY,
                              num2date, rrulewrapper, YearLocator,
                              MicrosecondLocator)
import sqlite3
import talib


class MyStrategy(bt.Strategy):

    def __init__(self):
            df =yf.download(tickers='AAPL', start='2021-01-01', interval="1d",rounding = True)
            df.head()
            price = [bar for bar in df['Close'] if bar != "NaN"]
            self.prices = np.array(price)
            RSI = talib.RSI(self.prices,14)
            SMA_20 = talib.SMA(self.prices, timeperiod=20)
            SMA_50 = talib.SMA(self.prices, timeperiod=50)




                        
                    #if price[x] > current_sma_20 and current_price > current_sma_50:
                    # if price[x] > price[x-1]+4 and price[x-1] > price[x-2]+4 and price[x-2] > price[x-3]:
                    #     print(talib.RSI(prices,14))

                        

    def next(self):
        #for x in range(len(self.prices)):
        if self.prices[0] > self.prices[-1]:
            current_price = self.prices[0]
            print(self.prices)
            self.buy_bracket(size= 10, limitprice=current_price*.05+current_price, price=current_price, stopprice=current_price-current_price*.025)
            pass
    
cerebro = bt.Cerebro()

df =yf.download('AAPL', start='2021-01-01', interval="5m",rounding = True)
feed = bt.feeds.PandasData(dataname = df)

cerebro.adddata(feed)
print(df)
cerebro.addstrategy(MyStrategy)
print(cerebro.broker.getvalue())
cerebro.run()
print(cerebro.broker.getvalue())
def saveplots(cerebro, numfigs=1, iplot=True, start=None, end=None,
            width=16, height=9, dpi=300, tight=True, use=None, file_path = '', **kwargs):

    from backtrader import plot
    if cerebro.p.oldsync:
        plotter = plot.Plot_OldSync(**kwargs)
    else:
        plotter = plot.Plot(**kwargs)

    figs = []
    for stratlist in cerebro.runstrats:
        for si, strat in enumerate(stratlist):
            rfig = plotter.plot(strat, figid=si * 100,
                                numfigs=numfigs, iplot=iplot,
                                start=start, end=end, use=use)
            figs.append(rfig)

    for fig in figs:
        for f in fig:
            f.savefig(file_path, bbox_inches='tight')
    return figs

saveplots(cerebro, file_path = 'static/savefig.png')

    
