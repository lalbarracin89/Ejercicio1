import numpy as np
import scipy
import matplotlib.pyplot as pp

def fitFunc(x):
	return pow(x,3) + pow(x,2) -4*x + 4
def derivada(x):
	return 3 * pow(x,2) + 2 * x - 4 
# 3*x**2


x=np.linspace(-5,5,100)
y=fitFunc(x)
ydiff=derivada(x)

pp.plot(x,y,x,ydiff)
pp.show()

