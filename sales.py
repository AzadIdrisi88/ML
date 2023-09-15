import matplotlib.pyplot as plt
import numpy as np 
categories = ['Apples', 'Oranges', 'Bananas', 'Grapes','Pineapple','Watermelon']
values1 = [20, 15, 10, 25,50,45]
plt.bar(categories, values1)
plt.plot(categories,values1)
plt.legend(['Sales 1'])
plt.title('Fruit Sales')
plt.xlabel('Fruit')
plt.ylabel('Number of Sales')
plt.savefig('sale.png')
plt.show()