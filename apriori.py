import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd
from apyori import apriori
store_data=pd.read_csv('input.csv',header=None)
store_data
print(store_data.shape)
records=[]
for i in range(0,21):
    records.append([str(store_data.values[i,j])for j in range(0,7)])
association_rule = apriori(records,min_support=0.10,min_confidence=0.5,min_lift=1.2, min_length=1)
association_results = list(association_rule)
print(len(association_results))
#print('\n',association_results)
for item in association_results:
    pair=item[0]
    items=[x for x in pair]
    print("rule:" +item[0] + "->" +items[1])
    print("Support:" +str(items[1]))
    print("Confidence:" +str(items[2][0][2]))
    print("Lift:" +str(items[2][0][3]))
    print("==============================================================================")