class tickerdataFinances:
    import re
    import urllib.request
    import requests
    from bs4 import BeautifulSoup
    import pymysql

    db=pymysql.connect("localhost","root","Msit@0066","yahoo")
    cursor=db.cursor()

    count=0
    rt=""
    income_str=" "
    file=open('ticker.txt','r')
    for i in file:
        rt = ""
        income_str = " "
        count += 1

        x = i.split(":")
        # print(x[1])
        symbol = x[0]

        url = "file:///C:/Users/naga kumari/PycharmProjects/yahoo/" + symbol + "/financials.html "
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read(), 'html.parser')
        #  print(soup.find_all('a'))
        print(url)

        '''Fetchingdata:TotalRevenue'''
        totrev = BeautifulSoup(str(soup.find_all(class_="Fz(s) Ta(end) Pstart(10px)")), 'html.parser')
        revenue = totrev.get_text().strip("[]")
        print("reve..", revenue)
        r = list(revenue)
        print(r)
        for q in r:
            rt += q
        print(rt)
        rtr = rt.split(" ")
        total_revenue = rtr[3].strip(",")
        print(total_revenue)

        '''Fetching data:Cost of Revenue'''
        cost_revenue = rtr[7].strip(",")
        print(cost_revenue)

        '''Fetching data:IncomeBefore Tax'''
        income_before = rtr[35].strip(",")
        print(income_before)

        '''Fetching data:NetIncome'''
        tr1 = BeautifulSoup(str(soup.find_all(class_="Fw(600) Ta(end) Py(8px) Pt(36px)")), 'html.parser')
        income= tr1.get_text().strip("[]")
        income_list=list(income)
        for il in income_list:
            income_str+=il
        print(income_str)
        print("inc",income_str[4])
        income_final=income_str.split(" ")
        total_income_revenue = income_final[len(income_final)-1].strip(",")
        print(total_income_revenue)


        '''inserting into Database'''
        sql = "INSERT INTO Finances(Fin_ticker,Total_Revenue,Cost_of_Revenue,Income_Before_Tax,Net_Income) VALUES (%s,%s,%s,%s,%s)"
        val = (symbol,total_revenue,cost_revenue,income_before,total_income_revenue)
        cursor.execute(sql, val)

        if(count==6):
            break

    db.commit()