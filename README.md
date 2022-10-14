# letstrade
letstrade is a free and open source stock trading bot written in Python. It is designed to support Alpaca API for now but our primary focus right now is adding more brokers. It contains backtesting, plotting and money management tools as well as strategy optimization.
This bot was inspired by Freqtrade which is a free and open source crypto trading bot.
Since this is connected to Alpaca is does support some crypto pairs but this bot was created for use with stocks. If you want a crypto trading bot use Freqtrade it would be better for crypto trading.
This bot hosted in a docker image and uses supervisord to run 2 executables at once so you get a simple UI to run back tests and manage stocks you are invested in while also having a trading bot running in the background. 
