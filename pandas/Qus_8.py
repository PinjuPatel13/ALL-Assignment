# 8. If you select a single column from the diamonds Data Frame, what will be the type of the 
# return value? 


import pandas as pd
import seaborn as sns

t=sns.load_dataset('diamonds')
#print(t)
#print(t.head(3))
print(t.depth)
print(type(t.depth))
