import pandas as pd
import matplotlib.pyplot as plt
DET=pd.read_csv('DET.csv')
a=DET.loc[:,['CHECK IN','STATUS']]

b=a.loc[:,'STATUS']
c = a.loc[:,'CHECK IN']
l={'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0}

for j in b:
    if j=='cancel':
        print(i)
        for i in l:
            for x in c:
                if i==x[3:5]:
                    l[i]+=1


plt.bar([1,2,3,4,5,6,7,8,9,10,11,12],l.values())
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

plt.show()
