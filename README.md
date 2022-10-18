# Lets trade start up guide.
Lets trade is an completely free and open source stock trading bot. Currently only supports Alpaca broker and aims to support more brokers such as TD Amera trade and more in the future. 

## About Letstrade 
Freqtrade is a free and open source stock trading bot written in Python. It is designed to support all major exchanges and be controlled via webUI and is inpsired from Freqtrade. It contains backtesting, plotting and money management tools as well as strategy optimization by machine learning.

## Disclamer
This software is for educational purposes only. Do not risk money which you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS.

Always start by running a trading bot in Dry-run and do not engage money before you understand how it works and what profit/loss you should expect.

We strongly recommend you to have coding and Python knowledge. Do not hesitate to read the source code and understand the mechanism of this bot.

## Supported Brokers 
-Right now only Alpca trade API is supported. 
Alpaca: https://alpaca.markets 

# Quickstart 
## Using lets trade with docker. 
This page explains how to run the bot with Docker. It is not meant to work out of the box. You'll still need to read through the documentation and understand how to properly configure it.
## Install Docker
Start by downloading and installing Docker CE for your platform: <br>
Mac: https://docs.docker.com/docker-for-mac/install/ <br>
Windows: https://docs.docker.com/desktop/install/windows-install/ <br>
Linux (ubuntu): 
1. apt update <br>
2. apt install apt-transport-https ca-certificates curl software-properties-common <br>
3. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg <br>
4. echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null <br>
5. apt update <br>
6. apt-cache policy docker-ce <br>
7. sudo apt install docker-ce <br>
8. apt install docker-compose <br>
9. docker-compose --version

## Install vscode 
if you are on mac or windows you are going to want to download vscode becasuse it makes running the docker compose easier. 
## Clone the git repo.
click on code then press download zip on the repo page. 
<img width="1680" alt="Screen Shot 2022-10-18 at 8 29 34 AM" src="https://user-images.githubusercontent.com/115838844/196429812-e91d28e5-a532-4d5f-a185-3fe61a311d9b.png">

## Get your api keys from your alpaca brokerage account. 
Go to Alpaca trade api and get your api key information. 
<img width="1680" alt="Screen Shot 2022-10-18 at 8 28 23 AM" src="https://user-images.githubusercontent.com/115838844/196430021-8a8dbadf-7bde-4e2f-bc3e-c17e374a1208.png">

## If you are using linux download winscp or cyberduck 
these are free programs that give you a graphical interface when working with linux devices. Linux can seem very confusing without a graphical guide to see what you are doing when first using it. These programs make it easier to get started and it is highly reccomened to run this bot on a linux linode server for the highest amount of reliability. 

## Go to Linode
We are not sponsored by Linode but are highly satisfied with the services they provide over any other cloud computing platform. If you would like to deploy this to a linux server you can go to linode.com and create a nanode. Linode gives you $100 in free cloud computing credits when you sign up and a nanode only cost about $5 per month so your first 20 months are free. <br>
<img width="1680" alt="Screen Shot 2022-10-18 at 8 44 46 AM" src="https://user-images.githubusercontent.com/115838844/196433549-ebec88d6-e598-4e74-90a3-ed45676a6ff1.png"> <br>

## Open up VScode if you are on Mac or Windows
You should download and open VSCode we recommend vscode in particular because it has docker extension which make running the docker file much easier. <br>
Press open folder and open the lettrade folder. It will contain a letstrade-bot folder 2 other files.
## Drag files into Linux machine if you are on Linux
We recommend using winscp or cyberduck to drag and drop you file but what ever way you like put the files on the machine. 

## Change the config file.
The config file is inside the letstrade-bot folder. That is where you should enter your Alpaca api key and secrect key and also the end point for if you want to paper trade or live trade. Make sure you save. 

## Compose docker file 

