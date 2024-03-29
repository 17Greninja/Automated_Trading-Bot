import datetime as dt
import yfinance
import pandas as pd
import mplfinance as fplt
from datetime import date
import stock_list
#import pyrenko
import math
import stock_list


listOfAllAvailableStocks = stock_list.Nifty50
renko_df = pd.DataFrame(columns=['Stock Name','Brick Size','Run','t_5%','t_10%','5%_t','10%_t'])
f = 1.5
backDelta = 0

score11 = {}


def getBrickSize(stockName):
   todays_date = date.today() - dt.timedelta(days = backDelta)
   yearAgo = str(todays_date.year-1) + '-' +str(todays_date.month)+'-'+str(todays_date.day)
   data = yfinance.download(stockName+'.NS', start=yearAgo)
   dates = list(data.index.values)
   dates = [str(x)[0:10] for x in dates]
   curPrice = data.loc[str(dates[-2-backDelta]),'Close']
   optimal_brick = curPrice*f/100
   #optimal_brick = pyrenko.renko().set_brick_size(auto = True, HLC_history = data[["High", "Low", "Close"]])
   return optimal_brick

def t10(percent,ohclv):
    dates = list(ohlcv.index.values)
    dates = [str(x)[0:10] for x in dates]
    start_date = dates[0]
    curPrice = ohlcv.loc[str(dates[0]),'Close']
    todayPrice = ohlcv.loc[str(dates[-1]),'Close']
    targetPrice = round((1-0.01*percent)*todayPrice,2)
    noOfDays = 0
    for i in range(1,31):
        if ohlcv.loc[str(dates[-1*i]),'Close'] <= targetPrice:
            noOfDays = i
            break
    if noOfDays == 0:
        ans = 0
    else:
        ans = noOfDays
    return ans

def increaseInLast(days,ohlcv):
    curPrice = ohlcv['Close'][-1]
    beforePrice = ohlcv.loc[str(dates[-1-days]),'Close']
    percent_increase = round((curPrice-beforePrice)*100/(beforePrice),2)
    return percent_increase
    
    
# Storing renko data - Each stock will have a renko dataframe assigned to it by a dictionary.
# stockToRenko = {} # dictionary - {'SBIN':renkoSBIN,'ADANI':renkoADANI,..........}
stockToRenko = {}
# count of red, green bars for sorting pupose stockName: [3,-4,5,...] - first list for green bars, 2nd for red bars
countGreenRedBars = {}

def updateRenko(stockName,curPrice,timeStamp,brickSize,renko):
    # update - add new bricks(if needed)
    numIndex = len(renko.index)
    numIndex -= 1
    stockDf = renko.copy()
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
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + dt.timedelta(days = ((1)/numNewBricks)*delta),"green",brickSize,lastUp+brickSize,lastUp]
                start = start + dt.timedelta(seconds=((1)/numNewBricks)*delta)
                lastUp += brickSize
        elif curPrice <= lastBottom:
            numNewBricks = int(math.floor((lastBottom-curPrice)/brickSize))
            if numNewBricks != 0:
                countGreenRedBars[stockName].append(-1*numNewBricks)
            lastBelow = lastBottom
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + dt.timedelta(days = ((1)/numNewBricks)*delta),"red",brickSize,lastBelow,lastBelow-brickSize]
                start = start + dt.timedelta(seconds=((1)/numNewBricks)*delta)
                lastBelow -= brickSize
    elif lastColor == "red":
        if curPrice>=lastTop:
            numNewBricks = int(math.floor((curPrice-lastTop)/brickSize))
            if numNewBricks != 0:
                countGreenRedBars[stockName].append(numNewBricks)
            lastBelow = lastTop
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + dt.timedelta(days = ((1)/numNewBricks)*delta),"green",brickSize,lastBelow+brickSize,lastBelow]
                start = start + dt.timedelta(seconds=((1)/numNewBricks)*delta)
                lastBelow += brickSize
        elif curPrice<=lastBottom:
            numNewBricks = int(math.floor((lastBottom-curPrice)/brickSize))
            if numNewBricks != 0:
                countGreenRedBars[stockName][-1] -= numNewBricks
            lastBelow = lastBottom
            for i in range(0,numNewBricks):
                stockDf.loc[len(stockDf.index)] = [stockName,start,start + dt.timedelta(days = ((1)/numNewBricks)*delta),"red",brickSize,lastBelow,lastBelow-brickSize]
                start = start + dt.timedelta(seconds=((1)/numNewBricks)*delta)
                lastBelow -= brickSize
    renko = stockDf.copy()
    return renko

for stockName in listOfAllAvailableStocks:
    countGreenRedBars[stockName] = []
    brickSize = round(getBrickSize(stockName),2)
    
    renko = pd.DataFrame(columns=["stock name","start timestamp","end timestamp","color","brick size","top price","bottom price"])
    start_date = dt.datetime.today()- dt.timedelta(365) # getting data of around 1 year.
    end_date = dt.datetime.today()
    ticker_name = stockName + ".NS"
    ohlcv = yfinance.download(ticker_name, start_date, end_date)
   
    score11_stock = 1

    dates = list(ohlcv.index.values)
    dates = [str(x)[0:10] for x in dates]
    start_date = dates[0]
    curPrice = ohlcv.loc[str(dates[0]),'Close']
    todayPrice = ohlcv.loc[str(dates[-1]),'Close']
   
   
    t_5 = t10(5,ohlcv)
    t_10 = t10(10,ohlcv)
    per_5days = increaseInLast(5, ohlcv)
    per_10days = increaseInLast(10, ohlcv)
    
    newPrice = curPrice
    rowNum = 0
    itDate = start_date
    # format
    format = '%Y-%m-%d'
    # convert from string format to datetime format
    itDate = dt.datetime.strptime(itDate, format)
    while abs(newPrice-curPrice)<brickSize and rowNum<len(ohlcv.index):
        itDate = itDate + dt.timedelta(1)
        if str(itDate.date()) in dates:
            rowNum += 1
            newPrice = ohlcv.loc[str(itDate.date()),'Close'] 
   
    numBricks = 0
    if newPrice == curPrice:
        numBricks = 0
    else:
        numBricks = math.floor(abs(newPrice-curPrice)/brickSize)
    finalDate = itDate
    itDate = dt.datetime.strptime(start_date, format)
    delta = finalDate - itDate
    delta = int(delta.days)
    if newPrice > curPrice:
        countGreenRedBars[stockName].append(numBricks)
    else:
        countGreenRedBars[stockName].append(-1*numBricks)
    for i in range(0,numBricks):
        if newPrice > curPrice:
            renko.loc[len(renko.index)] = [stockName,itDate,itDate+ dt.timedelta(days=((1)/numBricks)*delta),'green',brickSize,curPrice+brickSize,curPrice]   
            curPrice = curPrice + brickSize  
        else:
            renko.loc[len(renko.index)] = [stockName,itDate,itDate+ dt.timedelta(days=((1)/numBricks)*delta),'red',brickSize,curPrice,curPrice-brickSize]
            curPrice = curPrice - brickSize
        itDate = itDate + dt.timedelta(seconds=((1)/numBricks)*delta)
    while finalDate < end_date:
        finalDate = finalDate + dt.timedelta(1)
        if str(finalDate.date()) in dates:
            newPrice = ohlcv.loc[str(finalDate.date()),'Close']
            renko = updateRenko(stockName,newPrice,finalDate,brickSize,renko).copy()
    stockToRenko[stockName] = renko.copy()
    
    renko_df.loc[len(renko_df.index)] = [stockName,brickSize,countGreenRedBars[stockName][-1],t_5,t_10,per_5days,per_10days]

renko_df.to_excel("stock_values.xlsx")