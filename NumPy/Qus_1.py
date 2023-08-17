# Q.1 Convert a 1D array to a 2D array with 2 rows 
import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6])

arr_2d = arr_1d.reshape(2, -1)

print("Original 1D array:")
print(arr_1d)

print("\n2D array with 2 rows:")
print(arr_2d)
