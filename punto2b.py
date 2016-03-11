import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitFunc(x, a, b, c):
	return pow(x,a) + b*x + c


X=[7.5, 4.48, 8.60, 7.73, 5.28, 4.25, 6.99, 6.31, 9.15, 5.06]
Y=[28.66, 20.37, 22.33, 26.35, 22.29, 21.74, 23.11, 23.13, 24.68, 21.89]

fitParams, fitCovariances = curve_fit(fitFunc, X, Y)

Xarray=np.array(X)
lstX=np.linspace(Xarray.min(),Xarray.max(),100)
lstY=fitFunc(lstX,fitParams[0], fitParams[1], fitParams[2])

plt.ylabel('Eje X')
plt.xlabel('Eje Y')

# plot the data as red circles with errorbars in the vertical direction
plt.errorbar(X, Y, fmt = 'ro', yerr = 0.2)
# now plot the best fit curve and also +- 3 sigma curves
# the square root of the diagonal covariance matrix element 
# is the uncertianty on the corresponding fit parameter.
plt.plot(lstX,lstY)

plt.show()
