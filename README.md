# Automated_Trading-Bot
Design an automated trading bot, which sends updates and can be accessed through Telegram.

Problem Statement/ General Outline

1) Get OHLC data from API/web. 
    i)  timeperiod of ohlc data - 30 min candle
    ii) how many periods data we are using (eg past 1yr, 100 days)
    iii) how many stocks are we screening (50-100)
    iv) get OHLC data only once

2) Convert OHLC data into Renko Chart*
   i)  brick size (1 percent of 100 period average, etc..)
   ii) fixed or variable brick size
   iii) starting value of renko bar (in fixed brick-size algorithm)

3) Update current price into Renko Chart (whether a new bar is formed or not)
   i) How often are we getting current price (30 min)
   
4) Define entry conditions for Buying and exit conditions for selling

5) Send alert once entry/exit conditons are triggered

6) Place order through API or manually

7) How to choose which stocks to buy
   i)  Based on past behaviour (proprtional to average renko uptrend, can modify further)
   ii) How many stocks to invest in? (3-10)
   iii) How much to invest in each stock?
   iv) sector based?
   
8) Buffer money 

9) Negatively correlated stocks

10) Catastrophe condition - to detect unusual stock movement
   i) scan for stocks which moved x% in past y% days, invest more in them
   
*(There maybe a way to skip the conversion of data into renko charts, look into it..., will save time)

 