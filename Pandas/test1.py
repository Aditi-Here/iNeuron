import pandas as pd
df=pd.read_csv('C:/Drive_D/Ml_Material/iNeuron/Pandas/sample-csv/addresses.csv')
# print(df.head(10))
# print(df.dtypes)
# print(df.describe())
# print(df.dtypes==object)
df1=df[df.dtypes[df.dtypes==object].index]
# print(df1.describe())
# print(df1.columns)
# print(type[df1['city']])
# df1['adi']='aditi'
# print(df1.head())
# df_cat=pd.Categorical(df['id'])
# print(df_cat)
# it convert int to categorical data i.e. object type
# print(df['id'].isnull())
# print(df['city'].isnull()==True)

import numpy as np
# print(np.where(df['city'].isnull()==True))
# print(df['city'])
# print(df.columns)
# print(df.iloc[1])
# print(df.iloc[[1,2]])
# print((df.iloc[np.where(df['city']=='Belmont')])['country'])
# print(df['city'])

list_1=[10,46,33]
labels=['a','c','d']
arr=np.array(list_1)
# print(pd.Series(arr))
s1=pd.Series([1,2,3,5],index=['a','b','d','e'])
s2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
s3=s1*s2
# print(s3.iloc[0])
# print(s3.loc['a'])
from numpy.random import randn as rn
# print(rn(5,5))
# print(pd.DataFrame(rn(5,5)))
numpy_df=pd.DataFrame(rn(5,5),index=['a','b','c','d','e'],columns=['x','y',
                                                                   'z','u','v'])
# print(numpy_df)
# print(numpy_df.iloc[1])
# print(numpy_df.iloc[[0,3]]) it gives 0 and 3 row
# print(numpy_df.iloc[0:3])
# numpy_df['new_col']=numpy_df['x']+numpy_df['y']
# print(numpy_df)
# numpy_df.drop('new_col',axis=1,inplace=True)
# print(numpy_df)
