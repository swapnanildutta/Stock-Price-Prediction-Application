'''
IMPORTS
'''

import pandas as pd
import numpy as np
import random
from pickle import load
from tensorflow import keras

'''
Saved MODELS
'''
restored_model=keras.models.load_model('./model/microsoft_model.h5')
scaler = load(open('./model/scaler_microdpft.pkl', 'rb'))

def predict_high(stock_data: dict, n: int = 1 ):
    '''
    This function takes in a dataframe and returns a dataframe with the predicted high values for the next day
    '''
    data=pd.DataFrame(stock_data)
    data=data[5:]
    data=data['Time Series (Daily)']
    data=pd.DataFrame(data)
    data1=[[i['1. open'], i['4. close'], i['2. high']] for i in data['Time Series (Daily)']]
    data1=pd.DataFrame(data1, columns=['Open', 'Close', 'High'], index=data.index)
    data1=data1[:int(0.7*len(data1))]

    df=data1['High']
    arr=[]
    df=df[:60]
    for i in df:
        arr.append(i)
    arr=arr[::-1]
    ans1=0
    for i in range(n):
        df1=np.array(arr).reshape(-1, 1)
        df1=scaler.fit_transform(df1);
        dataset=[]
        a=df1[0:60, 0]
        dataset.append(a)
        dataset=np.array(dataset)
        dataset=dataset.reshape(dataset.shape[0], dataset.shape[1], 1)
        ans=restored_model.predict(dataset)
        ans=scaler.inverse_transform(ans)
        val=3*random.random();
        if random.randint(0,1)==1:
            val=val*1
        else:
            val=val*-1
        ans1=ans[0][0]
        arr.append(ans1)
        arr=arr[1:]
    return {'Prediction': str(ans1)}
