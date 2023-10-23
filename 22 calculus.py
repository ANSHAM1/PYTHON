from scipy.integrate import quad
from math import *


def f(x):
    return x*sin(x)

r,tt=quad(f,0,10)
print(r)

'''
quad - General Purpose Integration
dblquad - General Purpose Double Integration
nquad - General Purpose n- fold Integration
fixed_quad - Gaussian quadrature, order n
quadrature - Gaussian quadrature to tolerance
romberg - Romberg integration
trapz - Trapezoidal rule
cumtrapz - Trapezoidal rule to cumulatively compute integral
simps - Simpson's rule
romb - Romberg integration
polyint - Analytical polynomial integration (NumPy)
'''
srt="rr"


