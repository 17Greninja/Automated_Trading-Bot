# import yfinance as yf
# stock_info = yf.Ticker('ITC.NS').info
# # stock_info.keys() for other properties you can explore
# market_price = stock_info['regularMarketPrice']
# previous_close_price = stock_info['regularMarketPreviousClose']
# print('market price ', market_price)
# print('previous close price ', previous_close_price)

# from jugaad_data.nse import NSELive
# n = NSELive()
# q = n.stock_quote("HDFC")
# print(q['priceInfo'])
# import pyrenko
# import yfinance
# data = yfinance.download('TATASTEEL.NS', start="2022-11-01")
# print(type(data))
# optimal_brick = pyrenko.renko().set_brick_size(auto = True, HLC_history = data[["High", "Low", "Close"]])
# print(optimal_brick)
# objRenko = pyrenko.renko()
# print('Set brick size: ', objRenko.set_brick_size(auto = False, brick_size = optimal_brick))
# objRenko.build_history(prices = data.Close)
# print('Renko length:' , len(objRenko.get_renko_prices()))
# print('Renko bar directions: ', objRenko.get_renko_directions())
# print('Renko bar evaluation: ', objRenko.evaluate())
# objRenko.plot_renko()
# from datetime import date

# # today = date.today()
# # print("Today's date:", today-365)
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# # three_yrs_ago = datetime.now() - relativedelta(years=3)
# # print(three_yrs_ago)
# import datetime
# print(date.now() - date.timedelta(days=3*365))
# from datetime import date
  
# creating the date object of today's date
# todays_date = date.today()
  
# # printing todays date
# print("Current date: ", todays_date)
  
# # fetching the current year, month and day of today
# print("Current year:", todays_date.year-2000)
# print("Current month:", todays_date.month)
# print("Current day:", todays_date.day)
# todays_date = date.today()
# yearAgo = str(todays_date.year-1) + '-' +str(todays_date.month)+'-'+str(todays_date.day)
# print(yearAgo)
import test1
