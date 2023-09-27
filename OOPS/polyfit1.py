import numpy
from numpy.polynomial import polynomial as poly
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import random
import warnings
warnings.simplefilter('ignore', numpy.polynomial.polyutils.RankWarning)

x = [1, 2, 3, 4, 5]
# y=[2,5,7,9,11]
# y=[23,37,49,15,29]
# y = [3, 5, 7, 9, 11]
# y=[-13,18,-24,39,47]
# y=[121,76,49,14,186,13,22,20,44]#12
y=[130.45,135.00,132.60,131.00,129.60,132.80,129.50,131.40,129.50,132.40]
x=list(range(1,len(y)+1))
'''
Date	Open	High	Low	Close*	Adj Close**	Volume
Sep 20, 2023	130.45	131.80	128.00	128.30	128.30	43,613,463
Sep 18, 2023	135.00	135.00	130.05	130.45	130.45	62,420,823
Sep 15, 2023	132.60	133.30	129.85	131.95	131.95	85,058,495
Sep 14, 2023	131.00	134.20	130.80	131.70	131.70	58,800,620
Sep 13, 2023	129.60	130.50	127.70	129.55	129.55	23,371,459
Sep 12, 2023	132.80	133.15	128.65	129.00	129.00	38,065,283
Sep 11, 2023	129.50	131.85	129.20	131.15	131.15	33,377,857
Sep 08, 2023	131.40	131.65	129.20	129.50	129.50	34,313,523
Sep 07, 2023	129.50	130.80	128.60	130.15	130.15	30,268,235
Sep 06, 2023	132.40	12


130.45,135.00,132.60,131.00,129.60,132.80,129.50,131.40,129.50,132.40

'''
r = 5
model = poly.polyfit(x, y, deg=r)  # Generate the model
print(x, y, model)
plt.scatter(x, y)
# x=list(range(-5,10))
plt.plot(x, poly.polyval(x, model), "red", label="Degree " + str(r))
plt.legend()
plt.show()
# Get the model output formatted as a equation. Model is an nparray, poly1d requires the array of coefficients in reverse order. Hence th flip.
equation = str(numpy.poly1d(numpy.flip(model)))
print("The equation is Y=\n ", equation)
predictx = 12
predicty = poly.polyval(predictx, model)
# print(predictx, predicty)