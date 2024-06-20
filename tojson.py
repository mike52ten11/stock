# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:55:07 2023

@author: 621882
"""

import pandas as pd
import numpy as np
import datetime
import json
import jsonlines
from sklearn.model_selection import train_test_split

# function to add to JSON
def  write_json(content,filename = "train.jsonl"):
    with jsonlines.open(filename, mode='a') as writer:
        writer.write(content)
  

def text_example(context,name = 'pw_test.json'):
    Data = {}
    for i in range(1,len(context[:,0])):
        Date = context[i-1,0]
        Open = context[i-1,1]
        High = context[i-1,2]
        Low = context[i-1,3]
        Close = context[i-1,4]
        Volume  = context[i-1,6] 



        pred_Date = context[i,0]
        pred_Open = context[i,1]
        pred_High = context[i,2]
        pred_Low  = context[i,3]
        pred_Close = context[i,4]
        pred_Volume  = context[i-1,6]


        # Data["instruction"] = "你現在是預測大師，會根據我給的資訊來預測該用戶的下個時段的平均用電量,平均溫度,平均濕度,在不在家。" 
        Data["prompt"] = f"台股的交易時間是9:00 AM到01:30 PM你現在是預測大師，會根據我給的資訊來預測台股開盤價、最高價、最低價、收盤價、成交量，其中成交量非常重要。我給的資訊來:日期{Date}，開盤價{Open}、最高價{High}、最低價{Low}、收盤價{Close}、成交量{Volume}"
        Data["completion"] = f"預測日期{pred_Date}，預測開盤價{pred_Open}、預測最高價{pred_High}、預測最低價{pred_Low}、預測收盤價{pred_Close}、預測成交量{pred_Volume}。"
        
        if i%500==0:
            # print(f'==================j = {j}  CUS{j}_WEA.csv =================================')
            print('  i=',i)    
            print('  Data=\n',Data)    
        
        write_json(Data,filename = name)
        
if __name__ == '__main__':

    data = pd.read_csv(f'TWII_股票.csv')
    ytrain,ytest = train_test_split(data,
                                    train_size=0.9,
                                    shuffle=False)
    
    ytrain = ytrain.to_numpy()
    ytest = ytest.to_numpy()
    print(ytrain[0,:],len(ytrain))
    print(ytest[0,:],len(ytest))    
    Train_data = {} 
    Test_data = {}

    text_example(ytest,'stock_test.jsonl')
    text_example(ytrain,'stock_train.jsonl')
    


    









