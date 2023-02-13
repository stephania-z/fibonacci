import numpy as np 
import matplotlib.pyplot as plt

## 8.1 A Low-Pass Filter  
## Solving for V_out(t): dV_out/dt = (1/RC)*(V_in - V_out) when V_in(t)= 1 [if 2t --> even], V_in(t)= -1 [if 2t --> odd] 

RC = .1

def func(y, t):               #  y = V_out
  if (np.floor(2*t)%2==0):    ## V_in(t)= 1 [if 2t --> even]
    Vin = 1
  else:
    Vin = -1                  ## V_in(t)= -1 [if 2t --> odd] 
  return (1/RC)*(Vin - y)


a = 0     #from t=0 to t=10
b = 10
N = 10000
h = (b-a)/N

tlist  = np.arange(a, b, h)
ylist = []
y = 0

for t in tlist:                   ## iterations from t=0 to t=10
  ylist.append(y)                 ## appending new y value to a list for plotting
  k1 = h*func(y,t)                ## 4th order runge-kutta method
  k2 = h*func(y+0.5*k1, t+0.5*h)
  k3 = h*func(y+0.5*k2, t+0.5*h)
  k4 = h*func(y+k3, t+h)
  y = y + (1/6)*(k1+2*k2+2*k3+k4)

print(tlist)
print(ylist)



##plt.plot(tlist, 1000*np.exp(-tlist))
plt.plot(tlist, ylist)
