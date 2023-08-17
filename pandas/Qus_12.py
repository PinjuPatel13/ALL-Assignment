# 12. Plot a histogram of x, where x consists of 100,000 randomly-selected points with a normal 
# distribution (hint: you can use numpy.random.randn() to generate the random points). The 
# histogram should have 10 bins. Look at how the histogram changes when we try 20 and 50 
# bins. 

import numpy as np
import matplotlib.pyplot as plt

random_points = np.random.randn(100000)

bins_10 = 10
bins_20 = 20
bins_50 = 50

plt.figure(figsize=(12, 6))  


plt.subplot(1, 3, 1)
plt.hist(random_points, bins=bins_10, color='blue', edgecolor='black')
plt.title(f'Histogram ({bins_10} Bins)')
plt.xlabel('Value')
plt.ylabel('Frequency')


plt.subplot(1, 3, 2)
plt.hist(random_points, bins=bins_20, color='green', edgecolor='black')
plt.title(f'Histogram ({bins_20} Bins)')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
plt.hist(random_points, bins=bins_50, color='orange', edgecolor='black')
plt.title(f'Histogram ({bins_50} Bins)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()  
