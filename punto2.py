import numpy as np
import scipy
import matplotlib.pyplot as pp
from pylab import *
from scipy.optimize import curve_fit

X=[7.5, 4.48, 8.60, 7.73, 5.28, 4.25, 6.99, 6.31, 9.15, 5.06]
Y=[28.66, 20.37, 22.33, 26.35, 22.29, 21.74, 23.11, 23.13, 24.68, 21.89]

print X
print Y


pp.figure()
pp.scatter(X,Y, color='r',label='Punto 2')
pp.xlabel('Eje X')
pp.ylabel('Eje Y')
pp.show()

fitParams, fitCovariances = curve_fit(X, Y,1)
print fitParams
