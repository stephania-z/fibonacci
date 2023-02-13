import numpy as np
import math
import matplotlib.pyplot as plt

def func(x, t):
  return -x     ##differential equation to solve

a = 0
b = 2
h = 0.1
t = 0

tlist_e = [0]
xlist_e = [1000]

x = 1000

while (t<=b):          # iteration in step sizes of 0.1 from 0 to 2
  x = x + h*func(x, t) # using the euler method 
  t = t + h 
  xlist_e.append(x)    # appending values obtained to lists that can be plots
  tlist_e.append(t)
  #print(x, t)
  
print(xlist_e)
print(tlist_e)

plt.plot(tlist_e, xlist_e) # plot of euler's method for differentiation


def func(x, t):
  return -x     # differentiating with respect to t

a = 0      # differentiating between 0 and 2
b = 2
h = 0.1     # h is our step size for differentiating 
t = 0       

tlist_rk = [0]
xlist_rk = [1000]
x = 1000
#k1 = h*f(x,t)

while (t<=b):         # while t is less than or equal our upper limit b=2
  xlist_rk.append(x)  # we will evaluate each value of t using the 2nd order
  k1 = h*func(x,t)    # runge-kutta method
  k2 = h*func(x+0.5*k1, t+0.5*h)
  x = x + k2
  t = t+h
  tlist_rk.append(t)

print(xlist_rk)
print(tlist_rk)

plt.plot(tlist_rk, xlist_rk) #plot of our RK2 differentiation

plt.plot(tlist_e, xlist_e) #euler plot (orange)
