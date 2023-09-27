import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5,6,7,8,9,10]
y=[7,9,11,13,15,17,19,21,23,25]
plt.plot(x,y,color='red',linestyle='--')
plt.bar(x,y)
plt.savefig("img.png")
plt.show()