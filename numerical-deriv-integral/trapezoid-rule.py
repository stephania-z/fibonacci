import numpy as np
import math

def f(x):
  return np.sin(x)

N = 10
a = 0.0
b = 2.0
h = (b-a)/N

s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
  s += f(a+k*h)


print(h*s)
  
### output: 1.4160996313378889 when N = 100 --> .003% error
### output: 1.411423197098879 when N = 10 ---> 0.33% error
### accurate value: 1.4161468365 
