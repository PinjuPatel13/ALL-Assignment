# 11. Heights and initials of a group of individuals are provided below. Create a bar plot titled 
# “Height Comparison” to compare the heights among this group. 
# height = [179, 155, 191, 152, 188, 177] 
# names = ['QA', 'WB', 'EC', 'RD', 'TE', 'YF']

import matplotlib.pyplot as plt

height = [179, 155, 191, 152, 188, 177]
names = ['QA', 'WB', 'EC', 'RD', 'TE', 'YF']

plt.bar(names, height, color='blue')  
plt.xlabel('Names')  
plt.ylabel('Height')   
plt.title('Height Comparison')  
plt.ylim(0, max(height) + 10)  
plt.show()  
