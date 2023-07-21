import pandas as pd
man_log_data = { 'USERID' : ['MANAGER_1','MANAGER_2','MANAGER_3'],'PASSWORD':['SPECT_MAN1','SPECT_MAN2','SPECT_MAN3']}
man_log_data = pd.DataFrame(man_log_data)
rec_log_data = { 'USERID' : ['RECEP_1','RECEP_2','RECEP_3','RECEP_4','RECEP_5','RECEP_6'],'PASSWORD':['SPECT_REC1','SPECT_REC2','SPECT_REC3','SPECT_REC4','SPECT_REC5','SPECT_REC6'],'NAME':['RAHUL SUBRAMANIAM','PRITA ANAND','SHEENA K','TANMAY BHAT','SUSHANT S','RHEA C'],'MOBILE NUM':['9884840103','9876453811','8394628390','93647525347','7778394912','9385769400']}
rec_log_data = pd.DataFrame(rec_log_data)

print(rec_log_data.loc[0])

