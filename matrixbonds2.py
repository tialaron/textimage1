import os

from tinkoff.invest import Client, InstrumentStatus,GetAccruedInterestsRequest,CandleInterval, InstrumentIdType
from tinkoff.invest.exceptions import RequestError,AioRequestError
import cardid
import numpy as np
import pandas as pd
import json
import datetime

#filename1 = './bondsdata/BBG0000GXSD1_42.csv'
#filename2 = './bondsdata/BBG0000J5D76_0.csv'
#filename3 = './bondsdata/BBGHUYNYA015_8.csv'

def editordata(filemname):
    col_name = filemname[12:24]
    df1 = pd.read_csv(filemname)
    df1['datetime'] = pd.to_datetime(df1['datetime'])
    df1.index = df1['datetime']
    df1.drop('datetime',axis=1,inplace=True)
    df1.rename(columns={'real_value':col_name},inplace=True)
    return df1

#datafr1 = editordata(filename1)
#datafr2 = editordata(filename2)
#datafr3 = editordata(filename3)
#print(datafr1)

#df4 = pd.concat([datafr1,datafr2],axis=1)
#df5 = pd.concat([df4,datafr3],axis=1)
#print(df5)

list_direct = os.listdir('./bondsdata/')
print(list_direct)
print(len(list_direct))
print(type(list_direct))
file_name_list = []
for i in list_direct:
    file_name_list.append('./bondsdata/'+i)

df_new = pd.DataFrame()
for i in file_name_list:
    datafr_cur = editordata(i)
    df_new = pd.concat([df_new,datafr_cur],axis=1)
print(df_new)
df_new.to_csv('matrixbonds.csv')