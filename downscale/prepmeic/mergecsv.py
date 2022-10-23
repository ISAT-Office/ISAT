import pandas as pd
import os
files = os.listdir(".")
print(files)
for sect in ['power','residential','industry','transportation','agriculture']:
    file_list=[]
    for i in files:
        if (sect in i) and (".csv" in i):
           df = pd.read_csv(i)
           file_list.append(df)
    tmp = pd.concat(file_list)
    tmp2 = tmp.groupby(['ID','LAT','LON','sector'],as_index=False).sum()
    tmp2['month'] = 'annual'
    tmp2.to_csv(sect+"annual.csv",index=False)
    tmp=[]
    tmp2=[]
