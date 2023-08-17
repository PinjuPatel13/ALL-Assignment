# 3. Using NumPy, create a Pandas Data Frame with five rows and three columns. 
import numpy as np
import pandas as pd

data = np.random.rand(5, 3)

column_names = ['Column 1', 'Column 2', 'Column 3']

df = pd.DataFrame(data, columns=column_names)
print(df)
