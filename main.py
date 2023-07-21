import customer
import manager
import reception
import numpy as np
import pandas as pd
def main():
    print("\n\n------------WELCOME TO HOTEL SPECTRA------------\n")
    print('1.CUSTOMER')
    print('2.RECPTION')
    print('3.MANAGER')
    a = input('ENTER YOUR CHOICE')
    if a== '1' or a== 'CUSTOMER' or a == 'customer':
        customer.cust_log()
    elif a == '2' or a== 'RECEPTION' or a== 'reception':
        reception.recep_log()
    elif a == '3' or a== 'MANAGER' or a=='manager':
        manager.mana_log()

main()        

        
        
