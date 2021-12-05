import requests
import numpy as np
import pandas as pd
from io import StringIO
# visual
import matplotlib.pyplot as plt
import mplfinance as mpf
#matplotlib inline
import seaborn as sns
#finance
import talib
# time
import datetime as datetime
url='https://query1.finance.yahoo.com/v7/finance/download/VOO?period1=1607155311&period2=1638691311&interval=1d&events=history&includeAdjustedClose=true'
#反爬蟲
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# res = requests.get(url, headers=headers)
# print(res.status_code)
# print(res.content)
# s=res.content
# c=pd.read_csv(StringIO(s.decode('utf-8')),index_col = 'Date',parse_dates = ['Date'])
# print(c)
# c.Close.plot(figsize=(12,5))
while True:
    try:
        days = 24 * 60 * 60    #一天有86400秒 
        stock_id = 'voo'
        #input("請輸入股票代碼 : ",)
        time_start = '2021-10-01'
        #input("輸入開始日期 : ")
        time_end ='2021-11-30'
        # input("輸入結束日期 : ")
        initial = datetime.datetime.strptime( '1970-01-01' , '%Y-%m-%d' )
        start = datetime.datetime.strptime( str(time_start) , '%Y-%m-%d' )
        end = datetime.datetime.strptime( str(time_end), '%Y-%m-%d' )
        period1 = start - initial
        period2 = end - initial
        s1 = period1.days * days
        s2 = period2.days * days
        url = url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=" + str(s1) + "&period2=" + str(s2) + "&interval=1d&amp;events=history&amp;includeAdjustedClose=true"
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        response = requests.get(url, headers=headers)
        df = pd.read_csv(StringIO(response.text),index_col = "Date",parse_dates = ["Date"])
        # print(df)
        
        break
    except:
        print("輸入錯誤格式，請重新輸入")
# pic.show()

address = r"E:\\stock\\" + stock_id + ".csv"
df.to_csv(address)
#('csv file will be in E:\stock ')

df_voo=df
df_voo.index  = pd.DatetimeIndex(df_voo.index)
dfnew_voo = df_voo.drop(["Adj Close"],axis = 1)
# mpf.plot(dfnew_voo,type='candle')
stock_id = "voo"
mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
s  = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)
kwargs = dict(type='candle', mav=(5,10), volume=True, figratio=(20,15), figscale=1.2,title = stock_id, style=s)
# mpf.plot(dfnew_voo, **kwargs)

dfnew_voo['k'], dfnew_voo['d'] = talib.STOCH(dfnew_voo['High'], 
                                         dfnew_voo['Low'], 
                                         dfnew_voo['Close'], 
                                         fastk_period=9,
                                         slowk_period=3,
                                         slowk_matype=1,
                                         slowd_period=3,
                                         slowd_matype=1)

stock_id = "voo"
mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
s  = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)
add_plot =[mpf.make_addplot(dfnew_voo["k"],panel= 2,color="b"),
          mpf.make_addplot(dfnew_voo["d"],panel= 2,color="r")]
kwargs = dict(type='candle', mav=(5,10), volume = True,figsize=(20, 10),title = stock_id, style=s,addplot=add_plot)
mpf.plot(dfnew_voo, **kwargs)

# mpf.show()
