
import random as rd
import pandas as pd
import datetime as dt
import numpy as np
import smtplib 
from email.message import EmailMessage

def cust_log():
    ALL=pd.read_csv('ALL.csv')
    CUSTID=pd.read_csv('CUSTID.csv')
    print('')
    print('----- CUSTOMER SIGN IN -----')
    print('1.LOGIN')
    print('2.NEW')
    a=input('ENTER YOUR CHOICE:')
    print('')
    global cid
    if a== '1' or a== 'login':
        print('----CUSTOMER LOGIN----')
        
        cid = float(input('ENTER CUSTOMER ID:'))
        list_val = CUSTID['CUSTID'].tolist()
        if cid in list_val:
            cid=cid-1
            loca=CUSTID.PASS[cid]
            cid=cid+1
            c=input('enter password')
            if c == loca:
                print('')
                print('LOGIN SUCCESSFUL')
                cust()
                  
            else:
                print('')
                print('WRONG PASSWORD')
                
        else:
            print('')
            print('kindly give a valid id')
    elif a== '2':
       
        global passw
        for L in range(1,51):
            if CUSTID.loc[L-1,'T/NT'] == 'NT':
                cid=L
                
                print('your customer id is:',cid)
                passw=input('enter password')
                CUSTID.loc[L-1,'T/NT']='T'
                CUSTID.loc[L-1,'PASS']=passw
                CUSTID.loc[L-1,'CUSTID']=cid
                CUSTID.to_csv('CUSTID.csv',index=False)
                cust()
    else:
        print('enter a valid option')
        cust_log()

def book():
    roomt= pd.read_csv('Rooms.csv')
    DET=pd.read_csv('DET.csv')
    ALL=pd.read_csv('ALL.csv')
    print(" BOOKING ROOMS")
    name = str(input("Name: "))
    pn = str(input("Phone No.: "))
    add = str(input("Address: "))
    global ema
    ema = input('EMAIL : ')
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
            global dif
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
                typ=ALL.loc[i,'TYPE']
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'ROOM COST']=price*dif
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'DAYS']=dif
                ALL.loc[i,'EMAIL']=ema
                
                msg = EmailMessage()
                msg['Subject']='Reservation at Hotel SPECTRA'
                msg['From']='reservations.spectra@gmail.com'
                msg['To']=ema
                msg.set_content('Your '+typ+' has been reserved at Hotel Spectra \n from: '+ci+'\n to: '+co+'\n in the name of: '+name)
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login('reservations.spectra@gmail.com','rixcmkrkyczkidno')
                    smtp.send_message(msg)

                row=DET.shape[0]
                count=row
                DET.loc[count,'CUSTOMER NAME']=name
                DET.loc[count,'MOBILE NUM']=pn
                DET.loc[count,'ADDRESS']=add
                DET.loc[count,'CHECK IN']=ci
                DET.loc[count,'CHECK OUT']=co
                DET.loc[count,'ROOM COST']=price*dif
                DET.loc[count,'CUSTID']=cid
                DET.loc[count,'DAYS']=dif
                DET.loc[count,'ROOM NO.']=i+1
                DET.loc[count,'EMAIL']=ema
                DET.loc[count,'STATUS']='in'
                DET.loc[count,'ROOM TYPE']=roomt.loc[a,'TYPE']

                DET.to_csv('DET.csv',index=False)
                ALL.to_csv('ALL.csv',index=False)
                cust()
                break
            
        
    elif a== 1:
        for i in range(20,30):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                typ=ALL.loc[i,'TYPE']
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'ROOM COST']=price*dif
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'DAYS']=dif
                ALL.loc[i,'EMAIL']=ema
                
                msg = EmailMessage()
                msg['Subject']='Reservation at Hotel SPECTRA'
                msg['From']='reservations.spectra@gmail.com'
                msg['To']=ema
                msg.set_content('Your '+typ+' has been reserved at Hotel Spectra \n from: '+ci+'\n to: '+co+'\n in the name of: '+name)
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login('reservations.spectra@gmail.com','rixcmkrkyczkidno')
                    smtp.send_message(msg)

                row=DET.shape[0]
                count=row
                DET.loc[count,'CUSTOMER NAME']=name
                DET.loc[count,'MOBILE NUM']=pn
                DET.loc[count,'ADDRESS']=add
                DET.loc[count,'CHECK IN']=ci
                DET.loc[count,'CHECK OUT']=co
                DET.loc[count,'ROOM COST']=price*dif
                DET.loc[count,'CUSTID']=cid
                DET.loc[count,'DAYS']=dif
                DET.loc[count,'ROOM NO.']=i+1
                DET.loc[count,'EMAIL']=ema
                DET.loc[count,'STATUS']='in'
                DET.loc[count,'ROOM TYPE']=roomt.loc[a,'TYPE']
                

                DET.to_csv('DET.csv',index=False)
                ALL.to_csv('ALL.csv',index=False)
                cust()
                break
    elif a== 2:
        for i in range(30,40):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                typ=ALL.loc[i,'TYPE']
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'ROOM COST']=price*dif
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'DAYS']=dif
                ALL.loc[i,'EMAIL']=ema
                
                msg = EmailMessage()
                msg['Subject']='Reservation at Hotel SPECTRA'
                msg['From']='reservations.spectra@gmail.com'
                msg['To']=ema
                msg.set_content('Your '+typ+' has been reserved at Hotel Spectra \n from: '+ci+'\n to: '+co+'\n in the name of: '+name)
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login('reservations.spectra@gmail.com','rixcmkrkyczkidno')
                    smtp.send_message(msg)

                row=DET.shape[0]
                count=row
                DET.loc[count,'CUSTOMER NAME']=name
                DET.loc[count,'MOBILE NUM']=pn
                DET.loc[count,'ADDRESS']=add
                DET.loc[count,'CHECK IN']=ci
                DET.loc[count,'CHECK OUT']=co
                DET.loc[count,'ROOM COST']=price*dif
                DET.loc[count,'CUSTID']=cid
                DET.loc[count,'DAYS']=dif
                DET.loc[count,'ROOM NO.']=i+1
                DET.loc[count,'EMAIL']=ema
                DET.loc[count,'STATUS']='in'
                DET.loc[count,'ROOM TYPE']=roomt.loc[a,'TYPE']

                DET.to_csv('DET.csv',index=False)
                ALL.to_csv('ALL.csv',index=False)
                cust()
                break
    elif a== 3:
        for i in range(40,50):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                typ=ALL.loc[i,'TYPE']
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'ROOM COST']=price*dif
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'DAYS']=dif
                ALL.loc[i,'EMAIL']=ema
                
                msg = EmailMessage()
                msg['Subject']='Reservation at Hotel SPECTRA'
                msg['From']='reservations.spectra@gmail.com'
                msg['To']=ema
                msg.set_content('Your '+typ+' has been reserved at Hotel Spectra \n from: '+ci+'\n to: '+co+'\n in the name of: '+name)
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login('reservations.spectra@gmail.com','rixcmkrkyczkidno')
                    smtp.send_message(msg)

                row=DET.shape[0]
                count=row
                DET.loc[count,'CUSTOMER NAME']=name
                DET.loc[count,'MOBILE NUM']=pn
                DET.loc[count,'ADDRESS']=add
                DET.loc[count,'CHECK IN']=ci
                DET.loc[count,'CHECK OUT']=co
                DET.loc[count,'ROOM COST']=price*dif
                DET.loc[count,'CUSTID']=cid
                DET.loc[count,'DAYS']=dif
                DET.loc[count,'ROOM NO.']=i+1
                DET.loc[count,'EMAIL']=ema
                DET.loc[count,'STATUS']='in'
                DET.loc[count,'ROOM TYPE']=roomt.loc[a,'TYPE']

                DET.to_csv('DET.csv',index=False)
                ALL.to_csv('ALL.csv',index=False)
                cust()
                break
    elif a== 4:
        for i in range(50,55):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                typ=ALL.loc[i,'TYPE']
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'ROOM COST']=price*dif
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'DAYS']=dif
                ALL.loc[i,'EMAIL']=ema
                
                msg = EmailMessage()
                msg['Subject']='Reservation at Hotel SPECTRA'
                msg['From']='reservations.spectra@gmail.com'
                msg['To']=ema
                msg.set_content('Your '+typ+' has been reserved at Hotel Spectra \n from: '+ci+'\n to: '+co+'\n in the name of: '+name)
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login('reservations.spectra@gmail.com','rixcmkrkyczkidno')
                    smtp.send_message(msg)

                row=DET.shape[0]
                count=row
                DET.loc[count,'CUSTOMER NAME']=name
                DET.loc[count,'MOBILE NUM']=pn
                DET.loc[count,'ADDRESS']=add
                DET.loc[count,'CHECK IN']=ci
                DET.loc[count,'CHECK OUT']=co
                DET.loc[count,'ROOM COST']=price*dif
                DET.loc[count,'CUSTID']=cid
                DET.loc[count,'DAYS']=dif
                DET.loc[count,'ROOM NO.']=i+1
                DET.loc[count,'EMAIL']=ema
                DET.loc[count,'STATUS']='in'
                DET.loc[count,'ROOM TYPE']=roomt.loc[a,'TYPE']

                DET.to_csv('DET.csv',index=False)
                ALL.to_csv('ALL.csv',index=False)
                cust()
                break
    elif a== 5:
        for i in range(55,60):
            if ALL.loc[i,'STATUS'] == 'UNOCCUPIED':
                print('your room number is',i+1)
                typ=ALL.loc[i,'TYPE']
                ALL.loc[i,'STATUS']='OCCUPIED'
                ALL.loc[i,'CUSTOMER NAME']=name
                ALL.loc[i,'MOBILE NUM']=pn
                ALL.loc[i,'ADDRESS']=add
                ALL.loc[i,'CHECK IN']=ci
                ALL.loc[i,'CHECK OUT']=co
                ALL.loc[i,'ROOM COST']=price*dif
                ALL.loc[i,'CUSTID']=cid
                ALL.loc[i,'DAYS']=dif
                ALL.loc[i,'EMAIL']=ema
                
                msg = EmailMessage()
                msg['Subject']='Reservation at Hotel SPECTRA'
                msg['From']='reservations.spectra@gmail.com'
                msg['To']=ema
                msg.set_content('Your '+typ+' has been reserved at Hotel Spectra \n from: '+ci+'\n to: '+co+'\n in the name of: '+name)
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login('reservations.spectra@gmail.com','rixcmkrkyczkidno')
                    smtp.send_message(msg)

                row=DET.shape[0]
                count=row
                DET.loc[count,'CUSTOMER NAME']=name
                DET.loc[count,'MOBILE NUM']=pn
                DET.loc[count,'ADDRESS']=add
                DET.loc[count,'CHECK IN']=ci
                DET.loc[count,'CHECK OUT']=co
                DET.loc[count,'ROOM COST']=price*dif
                DET.loc[count,'CUSTID']=cid
                DET.loc[count,'DAYS']=dif
                DET.loc[count,'ROOM NO.']=i+1
                DET.loc[count,'EMAIL']=ema
                DET.loc[count,'STATUS']='in'
                DET.loc[count,'ROOM TYPE']=roomt.loc[a,'TYPE']

                DET.to_csv('DET.csv',index=False)
                ALL.to_csv('ALL.csv',index=False)
                cust()
                break
        

def cust():
    print('')
    print("\t\t\t 1 Booking\n") 
    print("\t\t\t 2 Restaurant\n") 
    print("\t\t\t 3 Payment\n")
    print("\t\t\t 4 Cancel Booking\n")
    print("\t\t\t 5 Exit\n")
    choice =int(input('enter your choice'))
    if choice == 1:
        book()
    elif choice == 2:
        food=pd.read_csv('restaurant.csv')
        roomno=int(input('enter your room number'))
        ALL=pd.read_csv('ALL.csv')
        print("-------------------------------------------------------------------------------------") 
        print("                                 Hotel SPECTRA") 
        print("-------------------------------------------------------------------------------------") 
        print("                                   Menu Card") 
        print("-------------------------------------------------------------------------------------") 
        print("\n BEVARAGES                                     23 Darjeeling momo........... 140.00") 
        print("---------------------------------------          24 Schezwan.................. 150.00") 
        print(" 0  Milk Shake.................. 190.00      ") 
        print(" 1  THAI Ice Tea................ 190.00          STARTERS") 
        print(" 2  Lemon Ice Tea............... 160.00          ------------------------------------") 
        print(" 3  Cold Coconut................ 130.00          25 Lettuce Wraps............. 250.00") 
        print(" 4  Fresh Lime Soda............. 100.00          26 Dragon Veggies............ 190.00") 
        print(" 5  Virgin Mojito............... 130.00          27 Vegetable Tempura......... 210.00") 
        print(" 6  Pina Colada................. 190.00          28 Vegetable Murtabak........ 210.00") 
        print(" 7  Lime Mint Cooler............ 130.00          29 S & P Mushroom............ 240.00") 
        print(" 8  Cappuccino.................. 150.00") 
        print(" 9  Mineral Water...............  30.00          MAIN COURSE")  
        print("                                                 ------------------------------------") 
        print(" SOUPS                                           30 Eggplant Steaks........... 450.00") 
        print("---------------------------------------          31 Aubergine Parmagiana...... 450.00") 
        print(" 10 Tom Yum..................... 110.00          32 Zucchini veeg Fritte...... 450.00") 
        print(" 11 Tom Kha..................... 110.00          33 Mushroom & Spinach                 ") 
        print("                                                    Cutlets................... 450.00") 
        print(" 12 Hot & Sour.................. 110.00          34 Potato 7 Feta Cakes....... 450.00") 
        print(" 13 Sweet Corn.................. 110.00          35 Courgette and Feta") 
        print(" 14 Veg. Munchow................ 110.00             Patties................... 450.00") 
        print("                                                 36 Ratatouille............... 450.00") 
        print(" STARTERS                                        37 Cottage Cheese Steak...... 450.00") 
        print("---------------------------------------          38 Mixed Vegetable ") 
        print(" 15 Crispy Chilli Balls......... 110.00             Shashlik.................. 450.00") 
        print(" 16 Crackling Spinach........... 110.00          39 Oven Baked Nicoise") 
        print(" 17 Cheese Wonton............... 120.00             Vegetable................. 450.00") 
        print(" 18 crispy corn crapes.......... 120.00") 
        print(" 19 Chilli Paneer............... 140.00          ") 
        print('                                                 DESERTS')
        print(" MOMOS (4 pcs)                                   ------------------------------------") 
        print(" --------------------------------------          40 Gelato Sundae............. 235.00") 
        print(" 20 Spicy Tofu.................. 140.00          41 Hot chocolate Sundae...... 235.00") 
        print(" 21 Tomato & Cheese............. 140.00          42 Fried Icecream............ 190.00") 
        print(" 22 Fried paneer................ 140.00          43 Elanir Payasam............ 190.00")
        TP=0
        x=1
        while x==1:
            choice = int(input('enter the dish number'))
            amt= int(input('enter amount'))
            price = food.loc[choice,'PRICE']
            tp = price*amt
            b=input('enter y if u want to order more')
            if b == 'y':
                x=1
                TP=TP+tp
            else:
                TP=TP+tp
                break
        RT=ALL.loc[roomno-1,'ROOM COST']
        ALL.loc[roomno-1,'REST COST']=TP
        TL=RT+TP
        ALL.loc[roomno-1,'TOTAL']=TL
        ALL.to_csv('ALL.csv',index=False)
        cust()

    elif choice == 3:
        DET= pd.read_csv('DET.csv')
        ALL = pd.read_csv('ALL.csv')
        a = input('DO YOU WANT TO CHECK OUT or JUST WANT TO SEE THE BILL')
        

        if a in ('bill','BILL'):
            roomno = int(input('ENTER YOUR ROOM NUMBER'))
            if ALL.loc[roomno-1,'STATUS'] == 'UNOCCUPIED':
                print('PLEASE ENTER THE CORRECT ROOM NUMBER')
            
            elif ALL.loc[roomno-1,'STATUS'] == 'OCCUPIED':

                ROOM_COST=ALL.loc[roomno-1,'ROOM COST']
                REST_COST=ALL.loc[roomno-1,'REST COST']                
                TOTAL=ROOM_COST+REST_COST
                t_18=TOTAL*(0.18)
                TT=TOTAL+t_18
               
                CUSTID = ALL.loc[roomno-1,'CUSTID']
                print('------------------------ HOTEL SPECTRA ------------------------')
                print()
                print('CUSTOMER ID           :',ALL.loc[roomno-1,'CUSTID'])    
                print('CUSTOMER NAME         :',ALL.loc[roomno-1,'CUSTOMER NAME'])
                print('MOBILE NUMBER         :',ALL.loc[roomno-1,'MOBILE NUM'])
                print('ADDRESS               :',ALL.loc[roomno-1,'ADDRESS'])       
                print('CHECK IN DATE         :',ALL.loc[roomno-1,'CHECK IN'])
                print('CHECK OUT DATE        :',ALL.loc[roomno-1,'CHECK OUT'])
                print('TOTAL NUMBER OF DAYS  :',ALL.loc[roomno-1,'DAYS'])                  
                print()
                print('---------------------------------------------------------------')
                print('ROOM                  :',ALL.loc[roomno-1,'TYPE'])
                print('ROOM COST             :','\t₹',ROOM_COST)
                print('RESTAURANT COST       :','\t₹',REST_COST)
                print('TOTAL(without tax)    :','\t₹',TOTAL)
                print('TAX: 18%              :','\t₹',t_18)
                print('TOTAL(with tax)       :','\t₹',TT)
                print()
                print('---------------------------------------------------------------')
                print('------------------------- THANK YOU ---------------------------')
                print('---------------- HOPE WE CURATED YOUR MEMORIES ----------------')
                print('---------- VISIT US AGAIN FOR MORE WONDERFUL EXPERIENCE -------')
                cust()
        elif a in ('CHECK OUT','check out'):
            roomno = int(input('ENTER YOUR ROOM NUMBER'))
            if ALL.loc[roomno-1,'STATUS'] == 'UNOCCUPIED':
                print('PLEASE ENTER THE CORRECT ROOM NUMBER')
            
            elif ALL.loc[roomno-1,'STATUS'] == 'OCCUPIED':
                ROOM_COST=ALL.loc[roomno-1,'ROOM COST']
                REST_COST=ALL.loc[roomno-1,'REST COST']
                TOTAL=ROOM_COST+REST_COST
                t_18=TOTAL*(0.18)
                TT=TOTAL+t_18
                pay=input('ENTER PAYMENT METHOD')
                    

                CUSTID = ALL.loc[roomno-1,'CUSTID']
                print('------------------------ HOTEL SPECTRA ------------------------')
                print()
                print('CUSTOMER ID           :',str(ALL.loc[roomno-1,'CUSTID']))    
                print('CUSTOMER NAME         :',ALL.loc[roomno-1,'CUSTOMER NAME'])
                print('MOBILE NUMBER         :',str(ALL.loc[roomno-1,'MOBILE NUM']))
                print('ADDRESS               :',ALL.loc[roomno-1,'ADDRESS'])       
                print('CHECK IN DATE         :',ALL.loc[roomno-1,'CHECK IN'])
                print('CHECK OUT DATE        :',ALL.loc[roomno-1,'CHECK OUT'])
                print('TOTAL NUMBER OF DAYS  :',str(ALL.loc[roomno-1,'DAYS']))                  
                print()
                print('---------------------------------------------------------------')
                print('ROOM                  :',ALL.loc[roomno-1,'TYPE'])
                print('ROOM COST             :','\t₹',ROOM_COST)
                print('RESTAURANT COST       :','\t₹',REST_COST)
                print('TOTAL(without tax)    :','\t₹',TOTAL)
                print('TAX: 18%              :','\t₹',t_18)
                print('TOTAL(with tax)       :','\t₹',TT)
                print('PAYMENT METHOD        :',pay)
                print()
                print('---------------------------------------------------------------')
                print('------------------------- THANK YOU ---------------------------')
                print('---------------- HOPE WE CURATED YOUR MEMORIES ----------------')
                print('---------- VISIT US AGAIN FOR MORE WONDERFUL EXPERIENCE -------')
                typ=ALL.loc[roomno-1,'TYPE']
                ci=ALL.loc[roomno-1,'CHECK IN']
                co=ALL.loc[roomno-1,'CHECK OUT']
                name=ALL.loc[roomno-1,'CUSTOMER NAME']
                ema = ALL.loc[roomno-1,'EMAIL']
                msg = EmailMessage()
                msg['Subject']='Booking Cancelled at Hotel SPECTRA'
                msg['From']='reservations.spectra@gmail.com'
                msg['To']=ema
                msg.set_content('You have checked out from your '+typ+' which you had booked \n from: '+ci+'\n to: '+co+'\n in the name of: '+name)
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login('reservations.spectra@gmail.com','rixcmkrkyczkidno')
                    smtp.send_message(msg)

                r=DET[DET['CUSTID']==CUSTID].index.values
                DET.loc[r[0],'STATUS']='out'    

                ALL.loc[roomno-1,'STATUS']='UNOCCUPIED'
                ALL.loc[roomno-1,'CUSTOMER NAME']=np.NaN
                ALL.loc[roomno-1,'MOBILE NUM']=np.NaN
                ALL.loc[roomno-1,'ADDRESS']=np.NaN
                ALL.loc[roomno-1,'CHECK IN']=np.NaN
                ALL.loc[roomno-1,'CHECK OUT']=np.NaN
                ALL.loc[roomno-1,'CUSTID']=np.NaN
                ALL.loc[roomno-1,'DAYS']=np.NaN
                ALL.loc[roomno-1,'EMAIL']=np.NaN
                ALL.loc[roomno-1,'ROOM COST']=0
                ALL.loc[roomno-1,'REST COST']=0
                ALL.loc[roomno-1,'TOTAL']=0
                ALL.loc[roomno-1,'TAX(18%)']=0
                ALL.loc[roomno-1,'TOTAL(tax)']=0

                pimpos=1
                while pimpos ==1:
                    numoro=int(input('HOW MANY STARS (out of 5) WOULD YOU LIKE TO GIVE TO OUR HOTEL AND OTHER SERVICES'))
                    if numoro == 1:
                        DET.loc[r[0],'STARS'] = 1
                        pimpos =2
                    if numoro == 2:
                        DET.loc[r[0],'STARS'] = 2
                        pimpos = 2
                    if numoro == 3:
                        DET.loc[r[0],'STARS'] = 3
                        pimpos = 2
                    if numoro == 4:
                        DET.loc[r[0],'STARS'] = 4
                        pimpos = 2
                    if numoro == 5:
                        DET.loc[r[0],'STARS'] = 5
                        pimpos = 2
                    if numoro not in (1,2,3,4,5):
                        print('PLEASE GIVE A VALID RATING')
                            
                DET.to_csv('DET.csv',index=False)
                ALL.to_csv('ALL.csv',index=False)

                
                
                exit()
                   
        else:
            print('ENJOY YOUR EXPERIENCE IN SPECTRA')
            cust()
    elif choice ==4:
        DET=pd.read_csv('DET.csv')
        ALL=pd.read_csv('ALL.csv')
        custid=int(input('enter customer id'))
        roomno=int(input('enter room number'))
        if custid == ALL.loc[roomno-1,'CUSTID']:
            can=input('do you want to cancel your booking')
            if ALL.loc[roomno-1,'REST COST']==0:        
                                                
                if can in('y','yes','YES','Y'):
                    typ=ALL.loc[roomno-1,'TYPE']
                    ci=ALL.loc[roomno-1,'CHECK IN']
                    co=ALL.loc[roomno-1,'CHECK OUT']
                    name=ALL.loc[roomno-1,'CUSTOMER NAME']
                    ema = ALL.loc[roomno-1,'EMAIL']
                    msg = EmailMessage()
                    msg['Subject']='Booking Cancelled at Hotel SPECTRA'
                    msg['From']='reservations.spectra@gmail.com'
                    msg['To']=ema
                    msg.set_content('Your '+typ+' booking \n from: '+ci+'\n to: '+co+'\n in the name of: '+name+'\n has been cancelled at Hotel Spectra')
                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                        smtp.login('reservations.spectra@gmail.com','rixcmkrkyczkidno')
                        smtp.send_message(msg)
                    print('CANCELLING YOUR BOOKING')

                    r=DET[DET['CUSTID']==custid].index.values
                    DET.loc[r[0],'STATUS']='cancel'    
                                        
                    ALL.loc[roomno-1,'STATUS']='UNOCCUPIED'
                    ALL.loc[roomno-1,'CUSTOMER NAME']=np.NaN
                    ALL.loc[roomno-1,'MOBILE NUM']=np.NaN
                    ALL.loc[roomno-1,'ADDRESS']=np.NaN
                    ALL.loc[roomno-1,'CHECK IN']=np.NaN
                    ALL.loc[roomno-1,'CHECK OUT']=np.NaN
                    ALL.loc[roomno-1,'CUSTID']=np.NaN
                    ALL.loc[roomno-1,'DAYS']=np.NaN
                    ALL.loc[roomno-1,'EMAIL']=np.NaN
                    ALL.loc[roomno-1,'ROOM COST']=0
                    ALL.loc[roomno-1,'REST COST']=0
                    ALL.loc[roomno-1,'TOTAL']=0
                    ALL.loc[roomno-1,'TAX(18%)']=0
                    ALL.loc[roomno-1,'TOTAL(tax)']=0

                    DET.to_csv('DET.csv',index=False)    
                    ALL.to_csv('ALL.csv',index=False)
                    print('BOOKING CANCELLED')
                    
                    cust_log()
                else:
                    print('enjoy your stay in SPECTRA')
                    cust()
            else:
                print('YOU CANT CANCEL YOUR BOOKING')
                cust()
        elif custid != ALL.loc[roomno-1,'CUSTID']:
            print('enter valid Customer ID')
            cust()
    elif choice ==5:
        exit()

            

        
        
        
        
