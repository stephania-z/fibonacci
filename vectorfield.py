import numpy as np
import matplotlib.pyplot as plt

k = 1
q = 1
q1 = -1

xlist = np.arange(-5, 5, 0.1) ## plots -5 to 5 intervals of 0.1 for x nd y
ylist = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(xlist, ylist) ## X and Y are arrays of 10,000 numbers 

## Ex = k*q*X/sgrt(x^2 + y^2) provides the x-component of the vector field
## Ey = k*q*X/sqrt(x^2 + y^2) gives the y-comp.

## r values used for each comp
r = np.sqrt(X**2+ Y**2) 
r1 = np.sqrt((X-1)**2 + (Y+4)**2)
r2 = np.sqrt((X+5)**2 + (Y-2)**2)

## the y and x comps. of our points are gven in the respectives equation
## electric field btwn (-5, 2) w/ +q and (1, -4) w/ -q
Ex = k*q*(X+5)/(r2**3) + k*q1*(X-1)/ (r1**3) 
Ey = k*q*(Y-2)/(r2**3) + k*q1*(Y+4)/ (r1**3) 

## X and Y are 1D arrays to form ggrid 
## Ex and Ey are 2D giving the coordinates of the point in e-field
plt.streamplot(X, Y, Ex, Ey, linewidth=1, density=1.2)

##labels for the plot
plt.xlabel("$X$")
plt.ylabel("$Y$")
plt.title("Electric Field")
plt.show()

