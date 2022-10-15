# letstrade
letstrade is a free and open source stock trading bot written in Python. It is designed to support Alpaca API for now but our primary focus right now is adding more brokers. It contains backtesting, plotting and money management tools as well as strategy optimization.
This bot was inspired by Freqtrade which is a free and open source crypto trading bot.
Since this is connected to Alpaca is does support some crypto pairs but this bot was created for use with stocks. If you want a crypto trading bot use Freqtrade it would be better for crypto trading.
This bot hosted in a docker image and uses supervisord to run 2 executables at once so you get a simple UI to run back tests and manage stocks you are invested in while also having a trading bot running in the background. 
# **Disclaimer**
This software is for educational purposes only. Do not risk money which you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS.

Always start by running a trading bot in Dry-run and do not engage money before you understand how it works and what profit/loss you should expect.

We strongly recommend you to have coding and Python knowledge. Do not hesitate to read the source code and understand the mechanism of this bot.

# supported brokers
Alpaca  https://app.alpaca.markets/login

# Quick Start Guide 
This section explains how to run the bot with Docker. It is not meant to work out of the box. You'll still need to read through the documentation and understand how to properly configure it.
### Install Docker ###
Start by downloading and installing Docker CE for your platform: <br>
Mac: https://docs.docker.com/desktop/install/mac-install/ <br>
Windows: https://docs.docker.com/desktop/install/windows-install/ <br>
Linux: https://docs.docker.com/get-docker/ <br>

### Clone Repo ###
Next Clone the git repo with either the git command if you have git cli installed or download the zip file from the github repo.
![image](https://user-images.githubusercontent.com/115838844/195992231-e347f91d-017d-4cba-ace0-817e64f0bde3.png)
Then download the repo which ever way you want to.
![image](https://user-images.githubusercontent.com/115838844/195992267-bf067a84-b32e-44ab-98e5-b8ce6fc8733e.png)

###Get your Alpaca API keys###
#### Either create or login to alpaca####
Letstrade is not sponsored or affiliated with alpaca trade api. This is the first of many brokers that will be available for you to connect to lets trade. <br>
![image](https://user-images.githubusercontent.com/115838844/195992872-ac947f67-c008-4062-9f1d-24cd489f3c7a.png)
#### Next get your API key, secret key and url endpoint.
![image](https://user-images.githubusercontent.com/115838844/195993478-a5e0e9ad-13dc-4d90-87af-fd54984928f9.png) <br>
If you want to switch from paper trading to live remove paper- from the url endpt. 
Once you see your API key and API secret key note it down somewhere safe. 
#### Do not share these numbers with anyone. ####




