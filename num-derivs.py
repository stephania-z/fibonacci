import numpy as np
import matplotlib.pyplot as plt

## numerically calculating derivatives
## forward difference method 

def deriv_sin(x, h = 0.001):
  return (np.sin(x + h) - np.sin(x))/h

print("Forward difference derivative:")  
print(deriv_sin(np.pi/3))


## central difference method below

def deriv_sin(x, h = 0.001):
  return ((np.sin(x + h) - np.sin(x - h)) / ((x + h) - (x - h)))

print("Central difference derivative:")
print(deriv_sin(np.pi/3))


## finite sum for second derivative 

def deriv_sin(x, h = 0.001):
  return ((np.sin(x + h/2) - np.sin(x - h/2)))/h

print("Finite sum for second derivative:")
print(deriv_sin(np.pi/3))
