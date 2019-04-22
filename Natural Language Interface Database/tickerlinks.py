import os
import requests
from bs4 import BeautifulSoup

count=0
file=open('ticker.txt','r')
for i in file:
    count+=1
    x = i.split(":")
    symbol = x[0]
    page1=requests.get('https://finance.yahoo.com/quote/'+symbol+'/profile?p='+symbol)
    page2=requests.get('https://finance.yahoo.com/quote/'+symbol+'/financials?p='+symbol)
    page3=requests.get('https://finance.yahoo.com/quote/'+symbol+'/key-statistics?p='+symbol)
    page4=requests.get('https://finance.yahoo.com/quote/'+symbol+'?p='+symbol)

    f1 = open('C:/Users/naga kumari/PycharmProjects/yahoo/'+symbol+'/profile.html', 'w')
    f2 = open('C:/Users/naga kumari/PycharmProjects/yahoo/'+symbol+'/financials.html', 'w')
    f3 = open('C:/Users/naga kumari/PycharmProjects/yahoo/'+symbol+'/statistics.html', 'w')
    f4 = open('C:/Users/naga kumari/PycharmProjects/yahoo/'+symbol+'/summary.html', 'w')

    if(page1.status_code==200):
        soup1=BeautifulSoup(page1.text,'html.parser')
        soup2 = BeautifulSoup(page2.text, 'html.parser')
        soup3 = BeautifulSoup(page3.text, 'html.parser')
        soup4 = BeautifulSoup(page4.text, 'html.parser')

        f1.write(str(soup1.encode("utf-8")))
        f2.write(str(soup2.encode("utf-8")))
        f3.write(str(soup3.encode("utf-8")))
        f4.write(str(soup4.encode("utf-8")))

        print("succesfull")
    if(count==6):
        break
