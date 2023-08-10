import pandas as pd

data = pd.read_csv('uk-500.csv')
#Selecting data by row numbers (.iloc)
#df=data.iloc[0:5,0:2] # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
#print(data.iloc[1]) # second row of data frame (Evan Zigomalas)
#print(data.iloc[-1]) # last row of data frame (Mi Richan)

#print(data.iloc[[5,7,9]])

#print(data.loc[data['first_name'] == 'Antonio', 'city':'email'])
#print(data.loc[(data['id'] > 100) & (data['id'] <= 200), ['postal', 'web']])
#print(data.loc[data['email'].str.endswith("gmail.com") & (data['first_name'] == 'Antonio')])

#print(data.loc[data['email'].str.endswith("gmail.com"),['first_name','last_name']])
#data.loc[data['email'].str.endswith("gmail.com"),'web']='Some value'
df =data.loc[data['email'].str.endswith("gmail.com"),['email','web']]
df.to_csv('test.csv',index=False)
