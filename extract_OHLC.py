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

listOfAllAvailableStocks = []

bufferMoney = 0
# Storing renko data - Each stock will have a renko dataframe assigned to it by a dictionary.
# stockToRenko = {} # dictionary - {'SBIN':renkoSBIN,'ADANI':renkoADANI,..........}
stockToRenko = {}
# allStocksData will have a df for each stock, will contain info about investments in that particular stock
# allStocksData = {}
# currentInvestment will contain data about all stocks and the amount of money currently invested in them.
# currentInvestment = {'test1':1000,'test2':2000}
currentInvestment = {}
# list of stock names
# allStocks = []
# actionLog = [['time1','invest','ADANI',1000],['time2','withdraw','MARUTI']]
actionLog = []
# count of red, green bars for sorting pupose stockName: [[3,5,2,4,45,...][5,6,3,1,3,1,2,....]] - first list for green bars, 2nd for red bars
countGreenRedBars = {}

def initializeRenko(stockName):
    # initial data
    return

# Each renko dataframe has these columns: ["stock name","start timestamp","end timestamp","color","brick size","top price","bottom price"]
def updateRenko(stockName,curPrice,timeStamp,brickSize):
    # update - add new bricks(if needed)
    numIndex = len(stockToRenko[stockName].index)
    numIndex -= 1
    stockDf = stockToRenko[stockName].copy()
    lastRow = stockDf.tail(1)

    lastTop = lastRow["top price"]
    lastTop = lastTop.to_frame().T
    lastTop = lastTop.loc['top price',numIndex]

    lastBottom = lastRow["bottom price"]
    lastBottom = lastBottom.to_frame().T
    lastBottom = lastBottom.loc['bottom price',numIndex]

    lastTimeStamp = lastRow["end timestamp"]
    lastTimeStamp = lastTimeStamp.to_frame().T
    lastTimeStamp = lastTimeStamp.loc['end timestamp',numIndex]

    lastColor = lastRow["color"]
    lastColor = lastColor.to_frame().T
    lastColor = lastColor.loc['color',numIndex]

    start = lastTimeStamp
    end = timeStamp
    delta = end - start
    delta = int(delta.days)
    if lastColor == "green":
        if curPrice >= lastTop:
            numNewBricks = int(math.floor((curPrice-lastTop)/brickSize))
            if numNewBricks != 0:
                countGreenRedBars[stockName][-1] += numNewBricks
            lastUp = lastTop
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + datetime.timedelta(days = ((1)/numNewBricks)*delta),"green",brickSize,lastUp+brickSize,lastUp]
                start = start + datetime.timedelta(seconds=((1)/numNewBricks)*delta)
                lastUp += brickSize
        elif curPrice <= lastBottom:
            numNewBricks = int(math.floor((lastBottom-curPrice)/brickSize))
            if numNewBricks != 0:
                countGreenRedBars[stockName].append(-1*numNewBricks)
            lastBelow = lastBottom
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + datetime.timedelta(days = ((1)/numNewBricks)*delta),"red",brickSize,lastBelow,lastBelow-brickSize]
                start = start + datetime.timedelta(seconds=((1)/numNewBricks)*delta)
                lastBelow -= brickSize
    elif lastColor == "red":
        if curPrice>=lastTop:
            numNewBricks = int(math.floor((curPrice-lastTop)/brickSize))
            if numNewBricks != 0:
                countGreenRedBars[stockName].append(numNewBricks)
            lastBelow = lastTop
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + datetime.timedelta(days = ((1)/numNewBricks)*delta),"green",brickSize,lastBelow+brickSize,lastBelow]
                start = start + datetime.timedelta(seconds=((1)/numNewBricks)*delta)
                lastBelow += brickSize
        elif curPrice<=lastBottom:
            numNewBricks = int(math.floor((lastBottom-curPrice)/brickSize))
            if numNewBricks != 0:
                countGreenRedBars[stockName][-1] -= numNewBricks
            lastBelow = lastBottom
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + datetime.timedelta(days = ((1)/numNewBricks)*delta),"red",brickSize,lastBelow,lastBelow-brickSize]
                start = start + datetime.timedelta(seconds=((1)/numNewBricks)*delta)
                lastBelow -= brickSize
    stockToRenko[stockName] = stockDf.copy()
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
    # slope>1, d(slope)/dt > 0, g_0/g_avg >=2.
    slope = getSlope(stockName)
    if slope<1:
        return False 
    doubleDerivative = getDoubleDerivative(stockName)
    if doubleDerivative<0:
        return False
    if scoreCatas2(stockName)<2:
        return False
    return True

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
        if stockToRenko[stockName].tail(1).loc[0].at["color"] == "red":
            return "take out"
        elif detectCatastrophe(stockName):
            return "catastrophe"
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
    return 0

def getPortfolio(stockName):
    # get the data of buy/sell of currently active stocks
    return currentInvestment

def amountToBuyCatas(s):
    # how much to invest in the stock s, given a catastrophe condition
    # think of an algorithm
    return 0

def getCurPrice(stockName):
    # returns the current price of stock stockName
    stock_info = yf.Ticker(stockName + ".NS").info
	# stock_info.keys() for other properties you can explore
    market_price = stock_info['regularMarketPrice']
    return market_price

def investInStock(stockName,quantity):
    # invest amount = amount in stock stockName - API
    print("Invest --- " + str(quantity) + " --- in ---" + stockName)
    if currentInvestment[stockName] == 0:
        currentInvestment[stockName] = quantity
    else:
        currentInvestment[stockName] += quantity
    return

def withdraw(stockName):
    # withdraw the money invested in the stock stockName - API
    print("Withdraw from --- " + stockName)
    curPrice = getCurPrice(stockName)
    bufferMoney += curPrice*currentInvestment[stockName]
    currentInvestment[stockName] = 0
    return

def log(signal,stockName,amount):
    # add in logs the action
    actionLog.append([time.time(),signal,stockName,amount])
    return

def log(signal,stockName):
    # add in logs the action
    actionLog.append([time.time(),signal,stockName])
    return

def score1(stockName):
    # 1) 4-7, 7>, 2-3
    score = 1
    greenBarCount = countGreenRedBars[stockName][-1]
    if greenBarCount < 0:
        return 0
    if greenBarCount > 7:
        score *= 2
    elif greenBarCount < 4:
        score *= 1
    else:
        score *= 3
    return

def score2(stockName):
    # API
    score = 1
    return score

def score3(stockName):
    # API
    score = 1
    return score

def score4(stockName): 
    #r1
    redBarCount = countGreenRedBars[stockName][-2] 
    score = 1
    if redBarCount>0:
        return 0
    score *= 1/abs(redBarCount)
    return score

def score5(stockName): 
    #average length of green run
    num = 0
    sum = 0
    for g in countGreenRedBars[stockName]:
        if g > 0:
            num += 1
            sum += g
    score = sum/num        
    return score

def score6(stockName):
    # 6) balance, sign changes
    signChanges = len(countGreenRedBars[stockName])-1
    sum_abs = 0
    for x in countGreenRedBars[stockName]:
        sum_abs += abs(x)
    score = math.log(sum_abs/signChanges)
    return score

def score7(stockName):
    # 7) probability (current)
    g0 = countGreenRedBars[stockName][-1]
    gteqg0 = 0
    gteqgoplus2 = 0
    for x in countGreenRedBars[stockName]:
        if x >= g0+2:
            gteqgoplus2 +=1
        elif x >= g0:
            gteqg0 +=1
    score = gteqgoplus2/gteqg0
    return score
    
def score8(stockName):
    # 7) probability (historical) 
    gteq1 = 0
    gteqg3 = 0
    for x in countGreenRedBars[stockName]:
        if x >= 3:
            gteqgoplus2 +=1
        elif x >= 2:
            gteqg0 +=1
    score = gteqg3/gteq1
    return score

def score9(stockName):
    # think
    score = 1
    return score

def score10(stockName):
    # think
    score = 1
    return score

def sortScore(stockName): #2, 3 , 9 , 10
    # score function for sorting purpose
    # score function depends on the following:
    # 1) 4-7, 7>, 2-3 done
    # 2) average price, period, standars deviation
    # 3) T_10% /momentum indicators
    # 4) number of red bars in past 
    # 5) average length of green bars in a run
    # 6) balance, sign changes
    # 7) probability (current)
    # 8) probablity (historical) 
    # 9) volume
    # 10) sector
    score = score1(stockName)*score2(stockName)*score3(stockName)*score4(stockName)*score5(stockName)*score6(stockName)*score7(stockName)*score8(stockName)*score9(stockName)*score10(stockName)
    return score

def getNumStocks(scoreList):
    # number of stocks to invest in from shouldInvestStocks
    return

def sortStocks(shouldInvestStocks):
    scoreList = []
    for stockName in shouldInvestStocks:
       score = sortScore(stockName)
       scoreList.append([stockName,score])
    #sort on basis of second list
    scoreList.sort(key=lambda x: x[1])
    numStocks = getNumStocks(scoreList)  #find
    return scoreList[:(-1*numStocks)]

def getSlope(stockName):
    # slope of price graph
    slope = 1
    return slope

def getDoubleDerivative(stockName):
    # double derivative of price graph
    doubleDerivative = 0
    return doubleDerivative

def scoreCatas1(stockName):
    # slope
    score = getSlope(stockName)
    return score

def scoreCatas2(stockName):
    # g_0/g_avg
    #average length of green run
    num = 0
    sum = 0
    for g in countGreenRedBars[stockName][:-1]:
        if g > 0:
            num += 1
            sum += g
    g_avg = sum/num
    score = countGreenRedBars[stockName][-1]/g_avg
    return score

def scoreCatas3(stockName):
    # x% increase in last y days - (x/y)
    score = 1
    return score

def sortCatasScore(stockName):
    score = scoreCatas1(stockName)*scoreCatas2(stockName)*scoreCatas3(stockName)
    return score

def sortCatastrophicStocks(catastropheStocks):
    # think of an algorithm
    scoreList = []
    for stockName in catastropheStocks:
        score = sortCatasScore(stockName)
        scoreList.append([stockName,score])
    scoreList.sort(key=lambda x: x[1])
    # Maximum of 2 stocks for catastrophe condition
    if len(scoreList) < 2:
        return scoreList
    return scoreList[:-2]

def investInStocks(shouldInvestStocks,catastropheStocks):
    # select stocks to invest in, and invest in them the correct amount of money
    finalStocks = sortStocks(shouldInvestStocks)
    finalStocksCatas = sortCatastrophicStocks(catastropheStocks)
    # bufferMoney = getBufferMoney()
    amountToBeInvested = bufferMoney*0.8
    amountToBeInvestedFinalStocks = amountToBeInvested*0.6
    amountToBeInvestedFinalStocksCatas = amountToBeInvested*0.4
    numFinalStocks = len(finalStocks)
    numCatasStocks = len(finalStocksCatas)
    for s in finalStocks:
        amount = amountToBeInvestedFinalStocks/numFinalStocks
        # amount = amountToBuy(s)
        curPrice = getCurPrice(s)
        quantity = math.floor(amount/curPrice)
        investInStock(s,quantity)
        bufferMoney -= quantity*curPrice
        log('invest',s,quantity)
        currentInvestment[s] += amount
    for s in finalStocksCatas:
        amount = amountToBeInvestedFinalStocksCatas/numCatasStocks
        # amount = amountToBuyCatas(s)
        curPrice = getCurPrice(s)
        quantity = math.floor(amount/curPrice)
        investInStock(s,quantity)
        bufferMoney -= quantity*curPrice
        log('catastrophe',s,quantity)
        currentInvestment[s] += amount
    return

def getBufferMoney():
    # get amount of money not invested - API
    return 0

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
    for s in listOfAllAvailableStocks:
        brickSize = getBrickSize(s)
        currentStockPrice = getCurPrice(s)
        updateRenko(s,currentStockPrice,time.time(),brickSize)
        signal =  signalFunction(s)
        # react according to signal
        match signal:
            case "invest":
                shouldInvestStocks.append(s)
            case "catastrophe":
                catastropheStocks.append(s)
            case "take out":
                withdraw(s)
                log("withdraw",s)
            case "wait":
                log("wait",s)
    investInStocks(shouldInvestStocks,catastropheStocks)
    pass

def testFunction():
    print("test completed")


timeout = 60.0*15 # 15 mins
# https://stackoverflow.com/questions/474528/how-to-repeatedly-execute-a-function-every-x-seconds
l = task.LoopingCall(mainFunction)
l.start(timeout) # call every 15 mins

reactor.run()