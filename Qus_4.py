# Q.4 Limit the number of items printed in python NumPy array a to a maximum of 6 
# elements. 
# Input: 
# array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) 


import numpy as np

a = np.array([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

np.set_printoptions(threshold=6)
print(a)
