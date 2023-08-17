# Q.2 Get the common items between a and b 
# Input: 
# a = np.array([1,2,3,2,3,4,3,4,5,6]) 
# b = np.array([7,2,10,2,7,4,9,4,9,8]) 

import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8]) 

a_set = set(a)
b_set = set(b)

common_items_set = a_set.intersection(b_set)
common_items_set = np.array(list(common_items_set))
print(type(common_items_set))
print("Common items using set intersection:", common_items_set)

