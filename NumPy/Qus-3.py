# Q.3 Get all items between 5 and 10 from a. 
# Input: 
# a = np.array([2, 6, 1, 9, 10, 3, 27])

import numpy as np
a = np.array([2, 6, 1, 9, 10, 3, 27])

mask = (a >= 5) & (a <= 10)
item = a[mask]
print("Between 5 and 10 ",item)
