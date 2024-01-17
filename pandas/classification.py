# classification 
# cut - is a pandas function used for classification
#       arguments for cut
#       column on which we want apply classification
#       bin - value range ( passed as list)
#       labels - categories 
#       returns a series

# what is classification
# name, marks
# sam   80
# pat  73
# bob  69
# tom  91

import pandas as pd

d1 = {
    'name': ['pat','sam','bob','tom','joe','brad','alice'],
    'age': [21,20,20,21,20,20,21],
    'marks': [69,71,87,91,58,78,63]
}

df = pd.DataFrame(d1)

#print(df)

# apply classification using 'cut'

df['grade'] = pd.cut(df['marks'],bins=[0,50,60,75,90,100], labels=['E','D','C','B','A'])

print(df)

