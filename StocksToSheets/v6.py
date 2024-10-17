import yfinance as yf
import csv
import pandas
import json
import os 
import discord


with open('data.txt', 'w') as f:
    f.write("\n")

with open('data.csv', 'w') as f:
    f.write("\n")
    f.write("ticker, price, trailingPE, forwardPE, oneYearChange, oneYearLow, oneYearHigh \n")
tickerlist = ["GOOGL", "GOOG", "AMZN", "AAPL", "COST", "IBM", "MSFT", "MRNA", "PFE", "KO", "NKE", "AMD", "TSLA"]
for ticker in tickerlist:
    
    tickerF = yf.Ticker(f'{ticker}').info
    price = '%.3f'%tickerF['currentPrice']
    trailingPE = '%.3f'%tickerF['trailingPE']
    forwardPE = '%.3f'%tickerF['forwardPE']
    oneYearChange = '%.3f'%tickerF['52WeekChange']
    oneYearHigh = '%.3f'%tickerF['fiftyTwoWeekHigh']
    oneYearlow = '%.3f'%tickerF['fiftyTwoWeekLow']
    # if(len(ticker) != 5): 
    #     if(ticker == 'GOOGL'): 
    #         break
    #     if(len(ticker) == 4):
    #         ticker = f"{ticker}     "
    #     if(len(ticker) == 3):
    #         ticker = f"{ticker}      "
    #     if(len(ticker) == 2):
    #         ticker = f"{ticker}       "
        
    dataset = [f"{ticker}", f"{price}", f"{trailingPE}", f"{forwardPE}", f"{oneYearChange}", f"{oneYearlow}",f"{oneYearHigh}"]
    with open('data.txt', 'a') as f:
        f.write(f"Data for ticker {ticker}: \n")
        for data in dataset:
            if data == dataset[6]: 
                f.write(str(data))
                f.write('\n')
                f.write('\n')
            else: 
                f.write(str(data))
                f.write('\n')

    with open('data.csv', 'a') as f:
        for data in dataset:
            if(data == dataset[6]): 
                f.write(str(data))
                f.write('\n')
            else: 
                f.write(str(data))
                f.write(',')

    df = pandas.read_csv('data.csv')
    # print(df)
    dp = df.to_string()


client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    channel = client.get_channel(1096698313752989739)
    print('We have logged in as {0.user}'.format(client))
    await channel.send(f"```{dp}```")

client.run(token='MTEyMzMxMTI5NjU0MTExMDI4Mg.G5SOUV.h9HFS1fLamUkyXBcRvhxRiFNCxMhElzBYToRps')
