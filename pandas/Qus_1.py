# 1. Compute the minimum, 25th percentile, median, 75th, and maximum of ser. 

import pandas as pd
import seaborn as sns

t=sns.load_dataset('flights')
# print(t)
new_data = pd.DataFrame.from_dict(t)
print(new_data.describe())
