# 10. Create an array of numbers between 0 and 6 with increments of 0.3 and name its “x”. 
# Then on the same plot, plot x, x², x³, and x⁴. For consistency, use the following style lines 
# respectively, “ro”, “bs”, “g”, and “:”. Lastly, make sure that the x-axis covers 0 to 6, while 
# the y-axis spans from 0 to 125. Do not worry if you are not familiar with the style lines — 
# you will recognize them as soon as you see the plot. 


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6.3, 0.3)

squared = x ** 2
cubed = x ** 3
fourth = x ** 4

plt.plot(x, x, 'ro', label='x')         
plt.plot(x, squared, 'bs', label='x²')  
plt.plot(x, cubed, 'g', label='x³')   
plt.plot(x, fourth, ':', label='x⁴')   

plt.xlabel('X')  
plt.ylabel('Y')  
plt.title('Powers of X')  
plt.xlim(0, 6)  
plt.ylim(0, 125)  
plt.legend()  
plt.grid(True)  
plt.show()  
