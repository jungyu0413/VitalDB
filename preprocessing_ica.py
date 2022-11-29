import vitaldb
import numpy as np
import pandas as pd

final_ica = pd.read_csv('/workspace/pre_data_df/final_ica.csv')


dt_list = []

dt_ppg_2400 = []
dt_ppg_1200 = []
dt_ppg_5 = []
dt_ppg_3 = []
dt_ppg_1 = []

dt_ecg_2400 = []
dt_ecg_1200 = []
dt_ecg_5 = []
dt_ecg_3 = []
dt_ecg_1 = []
lb_list = []
id = []
for idx in range(len(final_ica)):
    caseid, dt, label = final_ica.iloc[idx]
    vals_ppg_ecg = vitaldb.load_case(int(caseid), ['SNUADC/PLETH','SNUADC/ECG_II'], 1/100)
    vals_dt_ppg = vals_ppg_ecg[:, 0]
    vals_dt_ecg = vals_ppg_ecg[:, 1]
    
    if int(dt) > 0 and int(dt) < len(vals_dt_ppg) and int(dt) > 2400 and int(dt) < len(vals_dt_ecg) and int(dt) > 2400: 
        dt_list.append(dt)

        dt_ppg_2400.append(vals_dt_ppg[int(dt)-2400:int(dt)])
        dt_ppg_1200.append(vals_dt_ppg[int(dt)-1200:int(dt)])
        dt_ppg_5.append(vals_dt_ppg[int(dt)-300:int(dt)]) 
        dt_ppg_3.append(vals_dt_ppg[int(dt)-180:int(dt)]) 
        dt_ppg_1.append(vals_dt_ppg[int(dt)-60:int(dt)])
        
        dt_ecg_2400.append(vals_dt_ecg[int(dt)-2400:int(dt)]) 
        dt_ecg_1200.append(vals_dt_ecg[int(dt)-1200:int(dt)]) 
        dt_ecg_5.append(vals_dt_ecg[int(dt)-300:int(dt)]) 
        dt_ecg_3.append(vals_dt_ecg[int(dt)-180:int(dt)]) 
        dt_ecg_1.append(vals_dt_ecg[int(dt)-60:int(dt)])

        lb_list.append(label)
        id.append(caseid)
        print(caseid)

        if len(id) % 300 == 0:
            np.save('workspace/final_data/ica_id', id)
            np.save('workspace/final_data/ica_lb', lb_list)

            np.save('workspace/final_data/ica_ppg_2400', dt_ppg_2400)
            np.save('workspace/final_data/ica_ppg_1200', dt_ppg_1200)
            np.save('workspace/final_data/ica_ppg_5', dt_ppg_5)
            np.save('workspace/final_data/ica_ppg_3', dt_ppg_3)
            np.save('workspace/final_data/ica_ppg_1', dt_ppg_1)

            np.save('workspace/final_data/ica_ecg_2400', dt_ecg_2400)
            np.save('workspace/final_data/ica_ecg_1200', dt_ecg_1200)
            np.save('workspace/final_data/ica_ecg_5', dt_ecg_5)
            np.save('workspace/final_data/ica_ecg_3', dt_ecg_3)
            np.save('workspace/final_data/ica_ecg_1', dt_ecg_1)
            print('save!!')
        else:
            pass

    else:
        pass