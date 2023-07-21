import matplotlib.pyplot as plt
import pandas as pd
def mana_log():
    man_log_data = { 'USERID' : ['MANAGER_1','MANAGER_2','MANAGER_3'],'PASSWORD':['SPECT_MAN1','SPECT_MAN2','SPECT_MAN3'],'NAME':['ABHJIT PA','VIGNESH S','VIKRAM L']}
    man_log_data = pd.DataFrame(man_log_data)
    print("---- MANAGER LOGIN----")
    a=input("Enter your UserID:")
    li = man_log_data['USERID'].tolist()
    if a in li:
        b=input("Enter your Password")
        print("checking....")
        che = int(a[-1])
        if b == man_log_data.loc[che-1,'PASSWORD']:
            print('login successful')
            mana()
        else:
            print('WRONG PASSWORD')
    else:
        print('enter a valid USERID')


def mana():
    print("\t\t\t 1 Room Details\n") 
    print("\t\t\t 2 Staff Details\n")
    print("\t\t\t 3 Statistics\n")
    print("\t\t\t 4 Exit\n")
    choice =int(input('enter your choice'))
    if choice == 1:
        ALL=pd.read_csv('ALL.csv')
        print('\t 1 PARTICULAR ROOM\n')
        print('\t 2 ALL OCCUPIED ROOMS\n')
        print('\t 3 ALL UNOCCUPIED ROOMS\n')
        print('\t 4 ALL ROOMS\n')
        choice = input('ENTER YOUR CHOICE')
        if choice == '1':
            roomno = int(input('ENTER THE CUSTOMERS ROOM NUMBER'))
            print(ALL.loc[roomno-1,['ROOM NO.','TYPE','CUSTOMER NAME','MOBILE NUM','ADDRESS','CHECK IN','CHECK OUT','DAYS']])
            mana()
        elif choice == '2':
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            data=[]
            for i in range(0,60):            
                if ALL.loc[i,'STATUS']=='OCCUPIED':
                    a=ALL.loc[i,'ROOM NO.':'DAYS'].tolist()
                    data.append(a)
            d1=pd.DataFrame(data,columns=['ROOM NO.','TYPE','CUSTOMER NAME','MOBILE NUM','ADDRESS','CHECK IN','CHECK OUT','DAYS'])        
            print(d1)
            mana()
        elif choice == '3':
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            data=[]
            for i in range(0,60):            
                if ALL.loc[i,'STATUS']=='UNOCCUPIED':
                    a=ALL.loc[i,'ROOM NO.':'TYPE'].tolist()
                    data.append(a)
            d1=pd.DataFrame(data,columns=['ROOM NO.','TYPE'])        
            print(d1)
            mana()
        elif choice == '4':
            print(ALL.loc[0:60,'ROOM NO.':'DAYS'])
            mana()
    elif choice == 2:
        rec_log_data = { 'USERID' : ['RECEP_1','RECEP_2','RECEP_3','RECEP_4','RECEP_5','RECEP_6'],'PASSWORD':['SPECT_REC1','SPECT_REC2','SPECT_REC3','SPECT_REC4','SPECT_REC5','SPECT_REC6'],'NAME':['RAHUL SUBRAMANIAM','PRITA ANAND','SHEENA K','TANMAY BHAT','SUSHANT S','RHEA C'],'MOBILE NUM':['9884840103','9876453811','8394628390','93647525347','7778394912','9385769400']}
        rec_log_data = pd.DataFrame(rec_log_data)
        rs_data={'STAFFID':['RS_1','RS_2','RS_3','RS_4','RS_5','RS_6','RS_7','RS_8','RS_9','RS_10'],'NAME':['RAM T','RAJ M','KESHAV T','LALITH K','BALA A','KARAN M','PAVAN B','GUARAV I','AHUJA I','RAGAV P'],'MOBILE NUM':['9004000501','8989806050','9876098430','9080806078','9324536895','9967125646','8790865712','9070056634','9890795723','8809723156']}
        rs_data=pd.DataFrame(rs_data)
        hk_data={'STAFFID':['HK_1','HK_2','HK_3','HK_4','HK_5','HK_6','HK_7','HK_8','HK_9','HK_10'],'NAME':['ABHISHEK  R','ARJUN L','ANAND U','KARTHI K','VIVEK M','BASKAR J','SATISH E','SHANKAR I','EASWAR I','RAJIV B'],'MOBILE NUM':['9455542800','75-5678585','9955510072','9755500404','9955592118','9055549888','9255590739','8555707019','8555183269','9855576212']}
        hk_data=pd.DataFrame(hk_data)
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print('\t 1 PARTICULAR STAFFS\n')
        print('\t 2 ALL STAFFS\n')
        ch=input('ENTER YOUR CHOICE')
        if ch == '1':
            print('\t 1 RECEPTION STAFFS\n')
            print('\t 2 HOUSEKEEPING STAFFS\n')    
            print('\t 3 ROOM SERVICE STAFFS\n')
            choice = input('enter your choice')
            if choice== '1':
                ID=input('enter staff ID')
                che=int(ID[-1])-1
                print(rec_log_data.loc[che])
            elif choice == '2':
                ID=input('enter staff ID')
                che=int(ID[-1])-1
                print(hk_data.loc[che])
            elif choice == '3':
                ID=input('enter staff ID')
                che=int(ID[-1])-1
                print(rs_data.loc[che])
        elif ch == '2':
            print('\t 1 RECEPTION STAFFS\n')
            print('\t 2 HOUSEKEEPING STAFFS\n')    
            print('\t 3 ROOM SERVICE STAFFS\n')
            choice = input('enter your choice')
            if choice== '1':
                print(rec_log_data)
            elif choice == '2':
                print(hk_data)
            elif choice == '3':
                print(rs_data)
                    
    elif choice==3:
        print('\t 1 Bookings per month\n')
        print('\t 2 Reviews \n')
        ch=input('ENTER YOUR CHOICE')
        if ch == '1':
            DET=pd.read_csv('DET.csv')
            a=DET.loc[:,'CHECK IN']
            l={'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0}
            for i in l.keys():
                
                for j in a:
                    
                    if i== j[3:5]:
                        
                        l[i]+=1
            plt.bar([1,2,3,4,5,6,7,8,9,10,11,12],l.values())
            plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],['jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec'])
            plt.title('Bookings per Month')
            plt.show()
            mana()
        elif ch == '2':
            DET=pd.read_csv('DET.csv')
            a=DET.loc[:,'STARS']
            l={1:0,2:0,3:0,4:0,5:0}
            for i in l:
                for j in a:
                    if i==j:
                        l[i]+=1
            plt.bar([1,2,3,4,5],l.values())
            plt.xticks([1,2,3,4,5],['✩','✩✩','✩✩✩','✩✩✩✩','✩✩✩✩✩'])
            plt.title('REVIEWS')
            plt.show()
            mana()
    elif choice==4:                
        exit()

