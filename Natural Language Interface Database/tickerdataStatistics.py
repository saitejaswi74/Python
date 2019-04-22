class tickerdataStatistics:
    import re
    import urllib.request
    import requests
    from bs4 import BeautifulSoup
    import pymysql

    db=pymysql.connect("localhost","root","Msit@0066","yahoo")
    cursor=db.cursor()

    count=0
    sno=0
    file=open('ticker.txt','r')
    for i in file:
        count += 1
        sno+=1
        x = i.split(":")
        # print(x[1])
        symbol = x[0]

        url = "file:///C:/Users/naga kumari/PycharmProjects/yahoo/"+symbol+"/statistics.html"
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read(), 'html.parser')
        #  print(soup.find_all('a'))
        print(url)

        '''Fetching data:Market Capital'''
        marketcap= BeautifulSoup(str(soup.find_all(class_="Fz(s) Fw(500) Ta(end)")), 'html.parser')
        markt_income = marketcap.get_text().strip("[]")
        print("marketincome ", markt_income)
        market_list = markt_income.split(",")
        market = market_list[0]
        print("market",market)

        '''Fetching data:enterprise'''
        enterprise = market_list[1]
        print(enterprise)

        '''Fetching data:assets'''
        return_assets = market_list[15]
        print(return_assets)

        '''Fetching data:total_cash'''
        totcash = market_list[25]
        print(totcash)
        if(symbol=='NXPI' or symbol=='CGC' or symbol=='MGNX'):
            totcash=market_list[26]
            print("if",totcash)


        '''Fetch operating_cash_flow'''
        operate_cash = market_list[31]
        print(operate_cash)
        if(symbol=='NXPI' or symbol=='CGC' or symbol=='MGNX'):
            operate_cash = market_list[32]
            print("if",operate_cash)

        '''levered_free_cash_flow'''
        free_cash = market_list[32]
        if (symbol == 'NXPI' or symbol == 'MGNX'):
            free_cash = market_list[33]
        print(free_cash)

        '''Fetch total_debt'''
        total_debit = market_list[27]
        print(total_debit)
        if(symbol=='CMG' or symbol == 'NXPI' or symbol == 'MGNX' ):
            total_debit = market_list[28]
            print(total_debit)

        '''Fetch current_ratio'''
        current_ratio = market_list[29]
        print(current_ratio)
        if(symbol == 'NXPI' or symbol == 'MGNX' ):
            current_ratio = market_list[30]
            print(current_ratio)

        '''Fetch gross_profit'''
        profiit = market_list[20]
        print(profiit)
        if (symbol == 'MGNX'):
            profiit = market_list[21]
            print("if",profiit)

        '''Fetch proffit_margin'''
        margin = market_list[13]
        print(margin)
        if (symbol == 'CGC'):
            margin = market_list[14]
            print("if",margin)
        '''inserting into database'''
        sql = "INSERT INTO Statistics (sno,stat_ticker,marketcap,enterprise_value,return_on_assets,total_cash,operating_cash_flow,levered_free_cash_flow,total_debt,current_ratio,gross_profit,proffit_margin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(sno,symbol,market,enterprise,return_assets,totcash,operate_cash,free_cash,total_debit,current_ratio,profiit,margin)
        cursor.execute(sql, val)


        if (count == 6):
            break;

    db.commit()
