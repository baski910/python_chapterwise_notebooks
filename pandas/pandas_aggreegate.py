import pandas as pd
import dateutil
df=pd.read_csv('phone_data.csv')

print(df.head())

df['date']=df['date'].apply(dateutil.parser.parse,dayfirst=True)

#print(df.head())
#print(df.loc[df['item']=='call','duration'].sum())

#print(df.groupby(['item'])['duration'].aggregate(sum))

#print(df['duration'].max())

#print(df['duration'].describe())

#print(df['month'].value_counts())

print(df[df['item']=='call'].groupby(['month'])['duration'].sum())

print(df.groupby(['month']).aggregate({'duration':sum,'network_type': "count"}))

print(df.groupby(['month']).mean())

#Scikit Learn
