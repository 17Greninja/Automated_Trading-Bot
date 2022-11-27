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
    # ATR or score based
    brickSize = stockToRenko[stockName].tail(1)["bottom price"]/50
    return brickSize

def detectCatastrophe(stockName):
    # return true if condition is a catastrophe, else false
    # defination of catastrophe: 
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
        if detectCatastrophe(stockName):
            return "catastrophe"
        elif stockToRenko[stockName].tail(1).loc[0].at["color"] == "red":
            return "take out"
        else:
            return "wait"

def amountToBuy(stockName):
    # how much to invest given the current protfolio
    return

def getPortfolio(stockName):
    # get the data of buy/sell of currently active stocks
    return

def amountToBuyCatas(s):
    # how much to invest in the stock s, given a catastrophe condition
    return

def getCurPrice(stockName):
    # returns the current price of stock stockName
    return

def investInStock(stockName,amount):
    # invest amount = amount in stock stockName
    return
def withdraw(stockName):
    # withdraw the money invested in the stock stockName
    return

def log(signal,stockName,amount):
    # add in logs the action
    actionLog.append([time.time(),signal,stockName,amount])
    return

def log(signal,stockName):
    # add in logs the action
    actionLog.append([time.time(),signal,stockName])
    return

def investInStocks(shouldInvestStocks,catastropheStocks):
    #
    return

def totalRevenue():
    # returns the current holding plus the buffer money
    return



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