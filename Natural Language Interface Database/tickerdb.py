class tickerdb:
    import pymysql
    db=pymysql.connect("localhost","root","Msit@0066","yahoo")
    cursor=db.cursor()
    try:
        cursor.execute('Drop table  Profiles')
    except Exception as e:
        pass
    try:
        cursor.execute('Drop table  Statistics')
    except Exception as e:
        pass

    try:
        cursor.execute('Drop table Finances')
    except Exception as e:
        pass

    '''creating the tables'''
    try:
        cursor.execute("Create table Statistics(sno varchar(300),stat_ticker varchar(300) primary key,"
                       "marketcap varchar(300),enterprise_value varchar(300),"
                       "return_on_assets varchar(300),total_cash varchar(300),"
                       "operating_cash_flow varchar(300),levered_free_cash_flow varchar(300),"
                       "total_debt varchar(300),current_ratio varchar(300),gross_profit varchar(300),"
                       "proffit_margin varchar(300))")
        print("Statistics table created")
    except Exception as e:
        pass

    try:
        cursor.execute("create table Profiles(prof_ticker varchar(300)primary key,name varchar(300),"
                       "Address varchar(300),phonenum varchar(300),website varchar(300),"
                       "sector varchar(300),industry varchar(300),full_time varchar(300),"
                       "bus_summ varchar(300))")
        print("profiles table created")
    except Exception as e:
        pass

    try:
        cursor.execute('create table Finances(Fin_ticker varchar(300) primary key,Total_Revenue varchar(300),'
                       'Cost_of_Revenue varchar(300),Income_Before_Tax varchar(300),Net_Income varchar(300))')
        print("finances table created")
    except Exception as e:
        pass
