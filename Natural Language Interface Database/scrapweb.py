class scrapweb:
    import requests
    from bs4 import BeautifulSoup
    import os

    '''saving symbols and names into a file'''
    page=requests.get('https://finance.yahoo.com/trending-tickers')
    soup=BeautifulSoup(page.text,'html.parser')

    f=open('ticker.txt','w')

    table=BeautifulSoup(str(soup.find_all(class_='yfinlist-table W(100%) BdB Bdc($tableBorderGray)')),'html.parser')
    symbols=BeautifulSoup(str(table.find_all(class_='data-col0 Ta(start) Pstart(6px) Pend(15px)')),'html.parser')
    symbols_items=symbols.find_all('a')

    '''print(symbols_items)'''
    names=BeautifulSoup(str(table.find_all(class_='data-col1 Ta(start) Pstart(10px) Miw(180px)')),'html.parser')
    names_items=names.find_all();

    '''print(names_items)'''
    for i,j in zip(symbols_items,names_items):
        print(i.get_text())
        print(j.get_text())
        z=i.get_text()+":"+j.get_text()+"\n"
        f.write(z)

    '''creating directories'''
    count=0
    file=open('ticker.txt','r')

    for i in file:
        #print(i)
        x=i.split(":")
        #print(x[1])
        symbol=x[0]
        if(os.path.exists(x[0])):
            print("Directory already exists")
        else:
            os.mkdir(x[0])
            print('Directory Created')
        count+=1
        if(count==6):
            break

    '''fetching html into directories'''
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
