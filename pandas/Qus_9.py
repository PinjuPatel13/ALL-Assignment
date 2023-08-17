# 9. Create a line plot using the x and y values provided below. Label the y-axis as “Y” and 
# label the x-axis as “X”. 

import matplotlib.pyplot as plt

x = [3, 4, 5, 6]
y = [1.5, 2, 2.5, 3]

plt.plot(x, y, marker='o')  
plt.xlabel('X')
plt.ylabel('Y')  
plt.title('Line Plot')  
#plt.grid(True)  
plt.show()  
