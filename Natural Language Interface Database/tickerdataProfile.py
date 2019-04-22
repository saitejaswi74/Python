class tickerdataProfile:
    import re
    import urllib.request
    import requests
    from bs4 import BeautifulSoup
    import pymysql

    db=pymysql.connect("localhost","root","Msit@0066","yahoo")
    cursor=db.cursor()

    str_emp=" "
    count=0
    file=open('ticker.txt','r')
    for i in file:
        str_emp=" "
        count+=1
        x = i.split(":")
        #print(x[1])
        symbol = x[0]

        url="file:///C:/Users/naga kumari/PycharmProjects/yahoo/"+symbol+"/profile.html"
        page1 = urllib.request.urlopen(url)
        soup=BeautifulSoup(page1.read(),'html.parser')
        #  print(soup.find_all('a'))
        print(url)


        '''retrieving data from html page:name'''
        soup1=BeautifulSoup(str(soup.find_all(class_="Fz(m) Mb(10px)")),'html.parser')
        print("soup1",soup1)
        name=soup1.get_text().strip("[]")
        print(name)

        '''retrieving data from html page:address'''
        soup2=BeautifulSoup(str(soup.find_all(class_="D(ib) W(47.727%) Pend(40px)")),'html.parser')
        # print("soup2",soup2)
        add=soup2.get_text().strip("[]")
        address=re.sub(r'http\S+', '', add)
        print(address)

        '''retrieving data from html page:phonenum'''
        soup3=BeautifulSoup(str(soup.find_all(class_="D(ib) W(47.727%) Pend(40px)")),'html.parser')
        no=soup3.find('a')
        number=no.get_text()
        print(number)

        '''retrieving data from html page:Website'''
        emd=BeautifulSoup(str(soup.find_all(class_="D(ib) W(47.727%) Pend(40px)")),'html.parser')
        emm=emd.get_text().strip("[]")
        emailid=re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', emm)
        email=str(emailid).strip("[],''")
        print(email)

        '''Retrieving data:sector'''
        sec = BeautifulSoup(str(soup.find_all(class_="Fw(600)")), 'html.parser')
        sec1 = sec.get_text().strip("[]")
        print(sec1)
        sect = (sec1.split(","))
        sector = sect[0]
        print(sector)

        '''Retrieving data:Industries'''
        industries = sect[1]
        print(industries)

        '''Retrieving data:full time employee'''
        ft_emp = BeautifulSoup(str(soup.find_all(class_="Fw(600)")), 'html.parser')
        emp = ft_emp.get_text().strip("[]")
        # print(type(emp))
        emp1 = re.findall('[0-9]', emp)
        for z in emp1:
            str_emp += z
        print(str_emp)

        '''inserting into database'''
        sql="INSERT INTO Profiles(prof_ticker,name,Address,phonenum,website,sector,industry,full_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(symbol,name,address,number,email,sector,industries,str_emp)
        cursor.execute(sql,val)

        if (count == 6):
            break
    db.commit()
