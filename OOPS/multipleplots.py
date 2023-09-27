from matplotlib import pyplot as plt
import numpy
for i in range(10):
    d = int(6*numpy.random.random())+1
    # d=int(d*6)+1
    print(d, sep=",", end=",")
x = list(range(0, 11))
constant = [5 for x in x]
linear = [2*x - 3 for x in x]
quadratic = [3*x*x-x+9 for x in x]
random = [numpy.random.random()*300 for x in x]
# random=[int(6*numpy.random.random())+1 for x in x]
plt.plot(x, constant)
plt.plot(x, linear)
plt.plot(x, quadratic)
plt.plot(x, random)
plt.legend(["Constant", "Linear", "Quadratic", "Random"])
plt.show()