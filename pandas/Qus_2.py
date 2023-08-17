# 2. Creating A Pandas Data Frame and Using Sample Data Sets 
import pandas as pd
import seaborn as sns

Data_Set=sns.get_dataset_names()
print(Data_Set)

t=sns.load_dataset('tips')
new_data = pd.DataFrame.from_dict(t)
print(new_data)

