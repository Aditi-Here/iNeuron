#11 july 2021
import  pandas as pd
data={'a':[1,3,8],'b':[None,None,5],'c':[3,None,46]}
df_test=pd.DataFrame(data)
# print(df_test)
# print(df_test.dropna(thresh=2))
df_csv=pd.read_csv('C:/Drive_D/Ml_Material/iNeuron/Pandas/sample-csv/addresses.csv')
# print(df_csv.fillna(5))
# print(df_csv)
# print(df_csv.dropna(axis=1,inplace=True))
# df_csv.fillna(6)
# print(df_csv)
# print(df_csv.dropna(axis=1,inplace=True))
g=df_csv.groupby('city')
# print(g.mean())
# print(g.sum())
g1=g.sum()
# print(g1.loc['Belmont'])
# print(g1.transpose())
df_csv_1=df_csv
print(df_csv_1)