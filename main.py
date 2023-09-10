import mysql.connector as m
#setting up databse and tables
con =m.connect(host="localhost",user='root',passwd='Icecream')
cur=con.cursor(buffered=True)
cur.execute('create database Project')
cur.execute("show databases")
for i in cur:
    if(i[0].lower()=='project'):
        print("Database created successfully")
