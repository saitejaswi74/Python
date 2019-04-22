class Query:
    import pymysql

    f=open("StopWords.txt","r")
    list1=[]
    for k in f:
        k=k.replace('"','')
        list1.append(k.strip())
    #print(list1)

    q=input("Enter Question:\n")
    arr=[]
    qn=q.split(" ")
    for i in qn:
        #print(i)
        if i not in list1:
            arr.append(i)

    '''creating query'''
    def query_gen(arr,dict1,com,comp):
        From="com"
        a=""
        b=""
        n1="none"
        ticker=""
        where=""
        for i in arr:
            if 'wh' in i:
                select ="select"
                dict3=dict1.keys()
                #print(dict3)
            elif i in dict3:
                a=i
                b=dict1[i]
                if dict1[i]=="Profiles":
                    ticker="prof_ticker"
                elif dict1[i]=="Statistics":
                    ticker="stat_ticker"
                else:
                    ticker="Fin_ticker"
            elif i in com:
                n1=i
                From=i
        if n1=="none":
            return select+" "+a+" "+"from"+" "+b
        return select+" "+a+" "+"from"+" "+b+" "+"where"+" "+ticker+"='"+n1+"'"

    '''creating dict for tables in Database'''
    dict1={"stat_ticker" :"Statistics","marketcap":"Statistics","enterprise_value" :"Statistics","return_on_assets" : "Statistics","total_cash" : "Statistics","operating_cash_flow" :"Statistics","levered_free_cash_flow" :"Statistics","total_debt" : "Statistics","current_ratio" :"Statistics","gross_profit" :"Statistics","proffit_margin" :"Statistics","prof_ticker" :"Profiles","name" : "Profiles","Address" : "Profiles","phonenum" :"Profiles","website" : "Profiles","sector" : "Profiles","industry" :"Profiles","full_time" :"Profiles","bus_summ" :"Profiles","Fin_ticker" : "Finances","Total_Revenue": "Finances","Cost_of_Revenue": "Finances","Income_Before_Tax" : "Finances","Net_Income" : "Finances"}
    f=open("ticker.txt",'r')
    Tickername=list(f)
    symbols=[]
    n=[]
    for i in Tickername:
        j=i.split(":")
        symbols.append(j[0].strip())
        n.append(j[1].strip())
    que=query_gen(arr,dict1,symbols,n)
    conn=pymysql.connect("localhost","root","Msit@0066","yahoo")
    #try:
    cur=conn.cursor()
    cur.execute(que)
    print(que)
    rows=cur.fetchall()

    '''printing rows for given question'''
    for i in rows:
        print(i)
    #except:
        #print("Invalid Quary")
    conn.close()
