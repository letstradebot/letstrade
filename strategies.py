import backtrader as bt
import backtrader.indicators as btind
import backtrader.feeds as btfeeds



cerebro = bt.Cerebro()


class PointAnFigure(bt.Strategy):

    def __init__(self):
        self.dataclose = self.datas[0]
        
#def next goes through e
    def next(self):
        if not self.position: 
            if self.dataclose[0] > self.dataclose[-1]+4:
                if self.dataclose[-1] > self.dataclose[-2]+4 and self.dataclose[-2] > self.dataclose[-3]+4:
                    print(self.dataclose[0])
                    self.order = self.buy_bracket(size=.95*self.broker.cash/self.dataclose[0],limitprice=self.dataclose[0]*.1+self.dataclose[0], price=self.dataclose[0], stopprice=self.dataclose[0]-self.dataclose[0]*.025)
                    pass

class GoldenCross(bt.Strategy):

    #The Golden Cross is a candlestick pattern that is a bullish signal which a relatively short-term moving average crosses above a long-term moving average.
        #Specificaly this refers to the 50 day SMA corssing above the 200 day SMA
    #The Death Cross is a candle stick pattern that is a bearish signal which a short temr moving average crosses 

    def __init__(self) -> None:
        self.dataclose = self.datas[0]
        self.sma50 = btind.SimpleMovingAverage(period=50)
        self.sma200 = btind.SimpleMovingAverage(period=200)
        self.crossover = bt.indicators.CrossOver(self.sma50,self.sma200)
    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                self.order = self.buy(size=.95*self.broker.cash/self.dataclose[0])#self.buy_bracket(size=.95*self.broker.cash/self.dataclose[0],limitprice=self.dataclose[0]*.1+self.dataclose[0], price=self.dataclose[0], stopprice=self.dataclose[0]-self.dataclose[0]*.05)
                pass
        if self.position.size > 0:
            if self.crossover < 0:
                self.close()
                pass
class BuyNHold(bt.Strategy):

    def __init__(self) -> None:
        self.dataclose = self.datas[0]
        self.sma50 = btind.SimpleMovingAverage(period=50)
        self.sma200 = btind.SimpleMovingAverage(period=200)
        self.crossover = bt.indicators.CrossOver(self.sma50,self.sma200)
    def next(self):
        if self.dataclose[0]:
            self.order = self.buy(size=.95*self.broker.cash/self.dataclose[0])#self.buy_bracket(size=.95*self.broker.cash/self.dataclose[0],limitprice=self.dataclose[0]*.1+self.dataclose[0], price=self.dataclose[0], stopprice=self.dataclose[0]-self.dataclose[0]*.05)
            pass






print("code completed")