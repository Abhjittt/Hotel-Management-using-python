import pandas as pd
import datetime as dt
import numpy as np
ALL = pd.read_csv('ALL.csv')
a = input('DO YOU WANT TO CHECK OUT yes/no')
if a in ('y','Y','yes','YES'):
    roomno = int(input('ENTER YOUR ROOM NUMBER'))
    if ALL.loc[roomno-1,'STATUS'] == 'UNOCCUPIED':
        print('PLEASE ENTER THE CORRECT ROOM NUMBER')
        
    elif ALL.loc[roomno-1,'STATUS'] == 'OCCUPIED':
        TOTAL=ALL.loc[roomno-1,'TOTAL']
        ROOM_COST=ALL.loc[roomno-1,'ROOM COST']
        REST_COST=ALL.loc[roomno-1,'REST COST']
        cil=ALL.loc[roomno-1,'CHECK IN']
        col=ALL.loc[roomno-1,'CHECK IN']
        cil=cil.split('-')
        col=col.split('-')
        alpha = dt.date(int(cil[2]),int(cil[1]),int(cil[0]))
        beta = dt.date(int(col[2]),int(col[1]),int(col[0]))
        dif = (beta - alpha).days
        print('-------------- HOTEL SPECTRA --------------')
        print()
        print('CUSTOMER ID:',ALL.loc[roomno-1,'CUSTID'])    
        print('CUSTOMER NAME:',ALL.loc[roomno-1,'CUSTOMER NAME'])
        print('MOBILE NUMBER:',ALL.loc[roomno-1,'MOBILE NUM'])
        print('ADDRESS:',ALL.loc[roomno-1,'ADDRESS'])       
        print('CHECK IN DATE:',ALL.loc[roomno-1,'CHECK IN'])
        print('CHECK OUT DATE:',ALL.loc[roomno-1,'CHECK OUT'])
        print('TOTAL NUMBER OF DAYS:',dif)                  
        print()
        print('-------------------------------------------')
        print('ROOM :',ALL.loc[roomno-1,'TYPE'])
        print('ROOM COST         :','\t₹',ROOM_COST)
        print('RESTAURANT COST   :','\t₹',REST_COST)
        print('TOTAL(without tax):','\t₹',TOTAL)
        print('TAX: 18%          :','\t₹',ALL.loc[roomno-1,'TAX(18%)'])
        print('TOTAL(with tax)   :','\t₹',ALL.loc[roomno-1,'TOTAL(tax)'])
        print()
        print('-------------------------------------------')
        print('---------------- THANK YOU ----------------')
        print('------ HOPE WE CURATED YOUR MEMORIES ------')
        print('VISIT US AGAIN FOR MORE WONDERFUL EXPERIENCE')
        ALL.loc[roomno-1,'STATUS']='UNOCCUPIED'
        ALL.loc[roomno-1,'CUSTOMER NAME']=np.NaN
        ALL.loc[roomno-1,'MOBILE NUM']=np.NaN
        ALL.loc[roomno-1,'ADDRESS']=np.NaN
        ALL.loc[roomno-1,'CHECK IN']=np.NaN
        ALL.loc[roomno-1,'CHECK OUT']=np.NaN
        ALL.loc[roomno-1,'CUSTID']=np.NaN
        ALL.loc[roomno-1,'ROOM COST']=np.NaN
        ALL.loc[roomno-1,'REST COST']=np.NaN
        ALL.to_csv('ALL.csv',index=False)
       

else:
    print('ENJOY YOUR EXPERIENCE IN SPECTRA')
        
       
