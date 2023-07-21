import pandas as pd
import datetime as dt
import random as rd
import date
def book():
    roomt= pd.read_csv('Rooms.csv')
    ALL=pd.read_csv('ALL.csv')
    print(" BOOKING ROOMS")
    name = str(input("Name: "))
    pn = str(input("Phone No.: "))
    add = str(input("Address: "))
    if name!="" and pn!="" and add!="": 
        pass
                  
    else: 
        print("\tName, Phone no. & Address cannot be empty..!!") 
               
       
    print('ROOM TYPES')
    print(roomt)
    a = int(input('enter your choice'))
    price = roomt.loc[a,'RATE(per night)']
    b=1
    while b==1:
            global ci        
            global co
            ci = str(input('CHECK IN(y/m/d):'))
            co = str(input('CHECK OUT(y/m/d):'))
            c=1
            while c == 1:
                cil=ci.split('/')
                col=co.split('/')
                alpha = dt.date(int(cil[0]),int(cil[1]),int(cil[2]))
                beta = dt.date(int(col[0]),int(col[1]),int(col[2]))
                if alpha > beta :
                    print('error check out date must be after check in date')
                    b=2
                    c=2
                    exit()
                elif alpha == beta :
                    print('error check out date must be after check in date')
                    b=2
                    c=2
                    exit()
                elif alpha < beta:
                    dif = (beta - alpha).days
                    c=2
                    print('no.of days:',dif)
                    b=2
    if(a == 0):
        for i in range(0,20):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'TOTAL']=price
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'PASS']=passw
                ALL.to_csv('ALL.csv')
                break
            
        
    elif a== 1:
        for i in range(20,30):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'TOTAL']=price
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'PASS']=passw
                ALL.to_csv('ALL.csv')
                break
    elif a== 2:
        for i in range(30,40):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'TOTAL']=price
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'PASS']=passw
                ALL.to_csv('ALL.csv')
                break
    elif a== 3:
        for i in range(40,50):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'TOTAL']=price
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'PASS']=passw
                ALL.to_csv('ALL.csv')
                break
    elif a== 4:
        for i in range(50,55):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'TOTAL']=price
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'PASS']=passw
                ALL.to_csv('ALL.csv')
                break
    elif a== 5:
        for i in range(55,60):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'TOTAL']=price
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'PASS']=passw
                ALL.to_csv('ALL.csv')
                break
           
    
        
        
        
                
                


                
                
                    
