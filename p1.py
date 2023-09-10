import mysql.connector as m
con =m.connect(host="localhost",user='root',passwd='Icecream',database='Project')
cur=con.cursor(buffered=True)
password=1234 #for admin password

#menu for restaurant
d={"Momo":50,"French Fries":100,"Chilli Potato":80,"Chowmein":100,
   "VEG PLATE":400,"NON VEG PLATE":500,"South Indian meal":500,"MIX meal":600,
   "Ice Cream":80,"Gulab Jamun":30,"Ras Malai":50,"Gajar Halwa":60,"Pastry":150,
   "Chocolava Cake":250,"Burger":50,"Chocolate shake":80,"Oreo Shake":100,
   "Spring Roll":60,"Pav Bhaji":40,"Paneer Roll":150,"Mini Pizza":150,"Onion garlic free Plate":300}

def order():
    print("HELLO USER, Please enter your details")
    #Taking user information
    add=input("Enter address:- ")
    pincode=int(input("Enter your area pincode :- "))
    cont=int(input("Enter your 10 digit mobile no."))
    print("====================================")
    print("\t\tITEM\t\t\tPRICE")
    #printing menu items
    for i in d:
        m= "{:<30}".format(i)
        print('\t\t',m,":",d[i])
    it=input("Enter Item name(same as menu):- ")
    q=int(input("Enter quantity : "))
    amount=d[it]*q
    cur.execute("select * from restaurant where pincode=%s",(pincode,))
    r=cur.fetchall()
    if(len(r)==0):
        print("==============ALERT=================")
        print("No Restaurant available in your locality")
    else:
        print("Following are the restaurants available in your area")
        print("Rid\t\tRestaurant Name")
        for i in r:
            print(i[0],"\t\t",i[1])
    print("===========================================")
    res=int(input("Enter your preferred Restaurant id "))
    print("=========Order Confirmation================")
    print("===========================================")
    ck=input("Place Order:- (y/n) - ")
    if(ck.lower()=='y'):
        st=("insert into orders(amount,rid)" "values(%s,%s)")
        data=(amount,res)
        cur.execute(st,data)
        con.commit()
        cur.execute("select * from delboy where pincode=%s",(pincode,))
        r=cur.fetchone()
        phone=r[2]
        dname=r[1]

        print("ORDER PLACED SUCCESSFULLY")
        print("==========================")    
        print("++++++++++++BILL+++++++++\n")
        print("Ordered Item:- ",it)
        print("Quantity :- ",q)
        print("Total Amount :- ",amount)
        print("MODE OF PAYMENT:- COD")
        print("------------------------------")
        print("---------Delivery Details-----")
        print("NAME :-",dname)
        print("Contact:- ",phone)
        print("============================")
        print("--------HAPPY MEAL---------")


def addres():
    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
    print("ADD RESTAURANT")
    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n')
    print("Enter required details")
    a=int(input("Enter Restaurant id:- "))
    b=input("Enter Restaurant Name :- ")
    c=int(input("ENter 6 digit pincode for restaurant:- "))
    st=("Insert into restaurant(rid,rname,pincode)" "values(%s,%s,%s)")
    data=(a,b,c)
    cur.execute(st,data)
    con.commit()
    cur.execute('select * from restaurant where rid=%s',(a,))
    r=cur.fetchall()
    if(len(r)==1):
        print("Successfully Added")
     






def admin():
    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
    print('___________ADMIN PORTAL_____________')
    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
    p=int(input("Enter 4 digit pin:-"))
    while(p!=1234):
        p=int(input("Enter again"))
    print('Login success')
    print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
    print('1. GET REVENUE ')
    print('2. EXIT')
    c=int(input("Enter choice"))
    if(c==1):
        cur.execute('select amount from orders')
        s=0
        for i in cur:
            s=s+int(i[0])
        s=s*0.1
        print("Total revenue:- Rs.",s)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("=========================================================")
print('=========================WELCOME=========================')
print('=======================FOOD PORTAL=======================')
print("=========================================================")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("                  1. ORDER FOOD                                        ")
print("                  2. ADD RESTAURANT                                    ")
print("                  3. ADMIN PANEL                                       ")
print("                  4. EXIT PORTAL                                       ")

ch=int(input("Enter choice :- "))
while(ch!=4):
    if(ch==1):
        order()
    elif(ch==2):
        addres()
    elif(ch==3):
        admin()
    ch=int(input('Enter choice again :-'))

print("Happy meal , Visit again")




