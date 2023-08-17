# 4. For a Pandas Data Frame created from a NumPy array, what is the default behavior for 
# the labels for the columns? For the rows?

import numpy as np
import pandas as pd

data = np.random.rand(3, 3)

df = pd.DataFrame(data)

print("DataFrame:")
print(df)
print("\nColumn Labels:")
print(df.columns)
print("\nRow Labels (Index):")
print(df.index)
