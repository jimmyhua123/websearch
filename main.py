import requests
import pandas as pd
from io import StringIO
import datetime
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
        stock_id = input("請輸入股票代碼 : ",)
        time_start = input("輸入開始日期 : ")
        time_end = input("輸入結束日期 : ")
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
        print(df)
        df.Close.plot(figsize=(12,5))
        break
    except:
        print("輸入錯誤格式，請重新輸入")
address = r"E:\\stock\\" + stock_id + ".csv"
df.to_csv(address)
print('csv file will be in E:\stock ')