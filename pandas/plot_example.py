import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D 
 
countries = ['France','Spain','Sweden','Germany','Finland','Poland','Italy',
             'United Kingdom','Romania','Greece','Bulgaria','Hungary',
             'Portugal','Austria','Czech Republic','Ireland','Lithuania','Latvia',
             'Croatia','Slovakia','Estonia','Denmark','Netherlands','Belgium']
extensions = [547030,504782,450295,357022,338145,312685,301340,243610,238391,
              131940,110879,93028,92090,83871,78867,70273,65300,64589,56594,
              49035,45228,43094,41543,30528]
populations = [63.8,47,9.55,81.8,5.42,38.3,61.1,63.2,21.3,11.4,7.35,
               9.93,10.7,8.44,10.6,4.63,3.28,2.23,4.38,5.49,1.34,5.61,
               16.8,10.8]
life_expectancies = [81.8,82.1,81.8,80.7,80.5,76.4,82.4,80.5,73.8,80.8,73.5,
                    74.6,79.9,81.1,77.7,80.7,72.1,72.2,77,75.4,74.4,79.4,81,80.5]
data = {'extension' : pd.Series(extensions, index=countries), 
        'population' : pd.Series(populations, index=countries),
        'life expectancy' : pd.Series(life_expectancies, index=countries)}
 
df = pd.DataFrame(data)
df = df.sort_values('life expectancy')
"""
fig, axes = plt.subplots(nrows=3, ncols=1)
for i, c in enumerate(df.columns):
    df[c].plot(kind='bar', ax=axes[i], figsize=(12, 10), title=c)
plt.savefig('EU1.png', bbox_inches='tight')
"""
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.bar(df.index, df["extension"], color=(190/255,190/255,190/255,0.7), label='extension')
ax2.plot(df.index, df["population"], color='green', label='Hold')
ax.set_xticklabels(df_eg.index)
ax.legend(loc='best')
