import pandas as pd
def restaurant():
    food=pd.read_csv('restaurant.csv')
    roomno=int(input('enter your room number'))
    ALL=pd.read_csv('ALL.csv')
    print("-------------------------------------------------------------------------") 
    print("                           Hotel SPECTRA") 
    print("-------------------------------------------------------------------------") 
    print("                            Menu Card") 
    print("-------------------------------------------------------------------------") 
    print("\n BEVARAGES                            23 Darjeeling momo........ 140.00") 
    print("----------------------------------      24 Schezwan............... 150.00") 
    print(" 0  Milk Shake.............. 190.00      ") 
    print(" 1  THAI Ice Tea............ 190.00      STARTERS") 
    print(" 2  Lemon Ice Tea........... 160.00      --------------------------------") 
    print(" 3  Cold Coconut............ 130.00      25 Lettuce Wraps..........250.00") 
    print(" 4  Fresh Lime Soda......... 100.00      26 Dragon Veggies........ 190.00") 
    print(" 5  Virgin Mojito........... 130.00      27 Vegetable Tempura..... 210.00") 
    print(" 6  Pina Colada............. 190.00      28 Vegetable Murtabak.... 210.00") 
    print(" 7  Lime Mint Cooler........ 130.00      29 S & P Mushroom........ 240.00") 
    print(" 8  Cappuccino.............. 150.00") 
    print(" 9  Mineral Water...........  30.00      MAIN COURSE")  
    print("                                       ----------------------------------") 
    print(" SOUPS                                  30 Eggplant Steaks........ 450.00") 
    print("----------------------------------      31 Aubergine Parmagiana... 450.00") 
    print(" 10 Tom Yum................ 110.00      32 Zucchini veeg Fritter.. 450.00") 
    print(" 11 Tom Kha................ 110.00      33 Mushroom & Spinach            ") 
    print( "                                          Cutlets................ 450.00") 
    print(" 12 Hot & Sour............. 110.00      34 Potato 7 Feta Cakes.... 450.00") 
    print(" 13 Sweet Corn............. 110.00      35 Courgette and Feta") 
    print(" 14 Veg. Munchow........... 110.00         Patties................ 450.00") 
    print("                                        36 Ratatouille............ 450.00") 
    print(" STARTERS                               37 Cottage Cheese Steak... 450.00") 
    print("----------------------------------      38 Mixed Vegetable ") 
    print(" 15 Crispy Chilli Balls.... 110.00         Shashlik............... 450.00") 
    print(" 16 Crackling Spinach...... 110.00      39 Oven Baked Nicoise") 
    print(" 17 Cheese Wonton.......... 120.00         Vegetable.............. 450.00") 
    print(" 18 crispy corn crapes..... 120.00") 
    print(" 19 Chilli Paneer.......... 140.00      DESSERTS") 
    print(" MOMOS (4 pcs)                         ----------------------------------") 
    print(" ---------------------------------      40 Gelato Sundae.......... 235.00") 
    print(" 20 Spicy Tofu............. 140.00      41 Hot chocolate Sundae... 235.00") 
    print(" 21 Tomato & Cheese........ 140.00      42 Fried Icecream......... 190.00") 
    print(" 22 Fried paneer .......... 140.00      43 Elanir Payasam......... 190.00")
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
    RT=ALL.loc[roomno-1,'TOTAL']
    print(RT)
    TL=RT+TP
    print(TL)
    ALL.loc[roomno-1,'TOTAL']=TL
    print(ALL)
    ALL.to_csv('ALL.csv')
restaurant()

    
    
    
    
    
     

