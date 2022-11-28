from kiteconnect import KiteConnect
import pandas as pd
from datetime import datetime, timedelta
import os
import numpy as np
import math
import requests
import schedule
import time
import math
from twisted.internet import task, reactor
import pyrenko
import yfinance
from datetime import date
import yfinance as yf

listOfAllAvailableStocks = [
    'ADANIPORTS',
    'APOLLOHOSP',
    'ASIANPAINT',
    'AXISBANK',
    'BAJAJ-AUTO',
    'BAJFINANCE',
    'BAJAJFINSV',
    'BPCL',
    'BHARTIARTL',
    'BRITANNIA',
    'CIPLA',
    'COALINDIA',
    'DIVISLAB',
    'DRREDDY',
    'EICHERMOT',
    'GRASIM',
    'HCLTECH',
    'HDFCBANK',
    'HDFCLIFE',
    'HEROMOTOCO',
    'HINDALCO',
    'HINDUNILVR',
    'HDFC',
    'ICICIBANK',
    'ITC',
    'INDUSINDBK',
    'INFY',
    'JSWSTEEL',
    'KOTAKBANK',
    'LT',
    'M&M',
    'MARUTI',
    'NTPC',
    'NESTLEIND',
    'ONGC',
    'RELIANCE',
    'SBILIFE',
    'SHREECEM',
    'SBIN',
    'SUNPHARMA',
    'TCS',
    'TATACONSUM',
    'TATAMOTORS',
    'TATASTEEL',
    'TECHM',
    'TITAN',
    'UPL',
    'ULTRACEMCO',
    'WIPRO']

# Storing renko data - Each stock will have a renko dataframe assigned to it by a dictionary.
# stockToRenko = {} # dictionary - {'SBIN':renkoSBIN,'ADANI':renkoADANI,..........}
stockToRenko = {}
# allStocksData will have a df for each stock, will contain info about investments in that particular stock
allStocksData = {}
# currentInvestment will contain data about all stocks and the amount of money currently invested in them.
currentInvestment = {'test1':1000,'test2':2000}
# list of stock names
allStocks = []
actionLog = [['time1','invest','ADANI',1000],['time2','withdraw','MARUTI']]
# count of red, green bars for sorting pupose stockName: [[3,5,2,4,45,...][5,6,3,1,3,1,2,....]] - first list for green bars, 2nd for red bars
countGreenRedBars = {}

def initializeRenko(stockName):
    # initial data
    return

# Each renko dataframe has these columns: ["stock name","start timestamp","end timestamp","color","brick size","top price","bottom price"]
def updateRenko(stockName,curPrice,timeStamp,brickSize):
    # update - add new bricks(if needed)
    stockDf = stockToRenko[stockName]
    lastRow = stockDf.tail(1)
    lastTop = lastRow["top price"]
    lastBottom = lastRow["bottom price"]
    lastTimeStamp = lastRow["end timeStamp"]
    lastColor = lastRow["color"]
    start = lastTimeStamp
    end = timeStamp
    delta = end - start
    if lastColor == "green":
        if curPrice >= lastTop:
            numNewBricks = int(math.floor((curPrice-lastTop)/brickSize))
            lastUp = lastTop
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + timedelta(seconds = ((1)/numNewBricks)*delta),"green",brickSize,lastUp+brickSize,lastUp]
                start = start + timedelta(seconds=((1)/numNewBricks)*delta)
                lastUp += brickSize
        elif curPrice <= lastBottom:
            numNewBricks = int(math.floor((lastBottom-curPrice)/brickSize))
            lastBelow = lastBottom
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + timedelta(seconds = ((1)/numNewBricks)*delta),"red",brickSize,lastBelow,lastBelow-brickSize]
                start = start + timedelta(seconds=((1)/numNewBricks)*delta)
                lastBelow -= brickSize
    elif lastColor == "red":
        if curPrice>=lastTop:
            numNewBricks = int(math.floor((curPrice-lastTop)/brickSize))
            lastBelow = lastTop
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + timedelta(seconds = ((1)/numNewBricks)*delta),"green",brickSize,lastBelow+brickSize,lastBelow]
                start = start + timedelta(seconds=((1)/numNewBricks)*delta)
                lastBelow += brickSize
        elif curPrice<=lastBottom:
            numNewBricks = int(math.floor((lastBottom-curPrice)/brickSize))
            lastBelow = lastBottom
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + timedelta(seconds = ((1)/numNewBricks)*delta),"red",brickSize,lastBelow,lastBelow-brickSize]
                start = start + timedelta(seconds=((1)/numNewBricks)*delta)
                lastBelow -= brickSize
    stockToRenko[stockName] = stockDf
    return

def getBrickSize(stockName):
    # score based, better than ATR.
    todays_date = date.today()
    yearAgo = str(todays_date.year-1) + '-' +str(todays_date.month)+'-'+str(todays_date.day)
    data = yfinance.download(stockName+'.NS', start=yearAgo)
    optimal_brick = pyrenko.renko().set_brick_size(auto = True, HLC_history = data[["High", "Low", "Close"]])
    return optimal_brick

def detectCatastrophe(stockName):
    # return true if condition is a catastrophe, else false
    # defination of catastrophe: 
    # think of an algorithm
    return False 

def signalFunction(stockName):
    # run through given stock and return what to do
    # this will be run every 15 mins
    # run simultaneously for all the stocks
    # threading
    if currentInvestment[stockName] == 0:
        # if last 2 bars were green, then send invest signal
        # else send wait signal
        lastTwo = stockToRenko[stockName].tail(2)
        if detectCatastrophe(stockName):
            return "catastrophe"
        elif lastTwo.loc[0].at["color"] == "green" and lastTwo.loc[1].at["color"] == "green":
            return "invest"
        else:
            return "wait"
    else:
        # detect catastrophic condition, send catastrophic signal
        # if last bar was red, then pull out the invested money, send pull out signal
        currentInvestment[stockName] = getCurrentHoldings(stockName)
        if detectCatastrophe(stockName):
            return "catastrophe"
        elif stockToRenko[stockName].tail(1).loc[0].at["color"] == "red":
            return "take out"
        else:
            return "wait"

def getCurrentHoldings(stockName):
    # get current holding in the stock stockName
    if stockName in currentInvestment.keys():
        return currentInvestment[stockName]
    return 0

def amountToBuy(stockName):
    # how much to invest given the current protfolio
    # think of an algorithm
    return

def getPortfolio(stockName):
    # get the data of buy/sell of currently active stocks
    return currentInvestment

def amountToBuyCatas(s):
    # how much to invest in the stock s, given a catastrophe condition
    # think of an algorithm
    return

def getCurPrice(stockName):
    # returns the current price of stock stockName
    stock_info = yf.Ticker(stockName + ".NS").info
	# stock_info.keys() for other properties you can explore
    market_price = stock_info['regularMarketPrice']
    return market_price

def investInStock(stockName,amount):
    # invest amount = amount in stock stockName - API
    return
def withdraw(stockName):
    # withdraw the money invested in the stock stockName - API
    return

def log(signal,stockName,amount):
    # add in logs the action
    actionLog.append([time.time(),signal,stockName,amount])
    return

def log(signal,stockName):
    # add in logs the action
    actionLog.append([time.time(),signal,stockName])
    return

def sortStocks(shouldInvestStocks):
    # think of an algorithm
    return

def sortCatastrophicStocks(catastropheStocks):
    # think of an algorithm
    return

def investInStocks(shouldInvestStocks,catastropheStocks):
    # select stocks to invest in, and invest in them the correct amount of money
    finalStocks = sortStocks(shouldInvestStocks)
    for s in finalStocks:
        amount = amountToBuy(s)
        investInStock(s,amount)
    finalStocksCatas = sortCatastrophicStocks(catastropheStocks)
    for s in finalStocksCatas:
        amount = amountToBuyCatas(s)
        investInStock(s,amount)
    return

def getBufferMoney():
    # get amount of money not invested - API
    return

def totalRevenue():
    # returns the current holding plus the buffer money
    total = 0
    for s in currentInvestment:
        total += currentInvestment[s]
    total += getBufferMoney()
    return total

def mainFunction():
    shouldInvestStocks = []
    catastropheStocks = []
    for s in allStocks:
        brickSize = getBrickSize(s)
        currentStockPrice = getCurPrice(s)
        updateRenko(s,currentStockPrice,time.time(),brickSize)
        signal = signalFunction(s)
        # react according to signal
        match signal:
            case "invest":
                # invest money in the stock s
                # how much to invest?
                shouldInvestStocks.append(s)
                # amount = amountToBuy(s)
                # investInStock(s,amount)
                # log("invest",s,amount)
            case "catastrophe":
                # invest more in stock s
                # how much to invest more
                # maybe take out invested money from other stocks and invest here
                catastropheStocks.append(s)
                # amount = amountToBuyCatas(s)
                # investInStock(s,amount)
                # log("catastrophe",s,amount)
            case "take out":
                # take out the invested money from stock s
                withdraw(s)
                log("withdraw",s)
            case "wait":
                # do nothing
                log("wait",s)
    investInStocks(shouldInvestStocks,catastropheStocks)
    pass

timeout = 60.0*15 # 15 mins
# https://stackoverflow.com/questions/474528/how-to-repeatedly-execute-a-function-every-x-seconds
l = task.LoopingCall(mainFunction)
l.start(timeout) # call every 15 mins

reactor.run()