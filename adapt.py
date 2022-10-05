import numpy as np
import math

def f(x):
  return 2 * np.sqrt(1 - x**2)

Nprev = 10
a = -1.0
b = 1.0
delta = 0.000000001
eps = 1
Iprev = 3.0370488288835507

hprev = (b - a)/Nprev

s = 0.5*f(a) + 0.5*f(b)


while (np.abs(eps) > delta):
  Nnext = 2*(Nprev)
  hnext = hprev/2
  Inext = .5*Iprev + hnext*(np.sum(np.array([f(a+k*hnext) for k in range(1, Nnext, 2)])))
  
  eps = (Inext - Iprev)/3.0
  Iprev = Inext
  print(Iprev)
  Nprev = Nnext
  hprev = hnext



print(Inext)
