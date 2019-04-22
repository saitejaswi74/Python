import requests
from bs4 import BeautifulSoup

page=requests.get('https://finance.yahoo.com/trending-tickers')
soup=BeautifulSoup(page.text,'html.parser')

f=open('ticker.txt','w')

table=BeautifulSoup(str(soup.find_all(class_='yfinlist-table W(100%) BdB Bdc($tableBorderGray)')),'html.parser')
symbols=BeautifulSoup(str(table.find_all(class_='data-col0 Ta(start) Pstart(6px) Pend(15px)')),'html.parser')
symbols_items=symbols.find_all('a')
#print(symbols_items)
names=BeautifulSoup(str(table.find_all(class_='data-col1 Ta(start) Pstart(10px) Miw(180px)')),'html.parser')
names_items=names.find_all();
#print(names_items)
for i,j in zip(symbols_items,names_items):
    print(i.get_text())
    print(j.get_text())
    z=i.get_text()+":"+j.get_text()+"\n"
    f.write(z)