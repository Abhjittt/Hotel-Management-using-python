import datetime as dt
def datey():
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
                    elif alpha == beta :
                        print('error check out date must be after check in date')
                        b=2
                        c=2
                    
                    elif alpha < beta:
                        dif = (beta - alpha).days
                        c=2
                        print('no.of days:',dif)
                        b=2

