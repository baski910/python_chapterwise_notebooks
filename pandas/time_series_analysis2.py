import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import dateutil

#data=sm.datasets.co2.load_pandas()
#co2=data.data
co2=pd.read_csv('/usr/local/lib/python3.5/dist-packages/statsmodels/datasets/co2/co2.csv')

print(co2.head())
def f(x):
	return dateutil.parser.parse(str(x))

co2['datetime']=co2['date'].apply(f)

print(co2.head())
co2.set_index(pd.DatetimeIndex(co2['datetime']),inplace=True) # inplace witll change the dataframe itself
print(co2.index)
co2.drop(['date'],axis=True,inplace=True)
#print(co2.head())
y = co2['co2'].resample('MS').mean() # frequency calculated from Month Start. for  month end M
				     # http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
print(y.head())



#print(y['1990':])
#print(y['1995-10-01':'1996-10-01'])

#print(y.isnull().sum())

y=y.fillna(y.bfill())  # bfill/backfill  or ffill/pad

#print(y.isnull().sum())

y.plot(figsize=(15,6))

plt.show()
'''
'''
