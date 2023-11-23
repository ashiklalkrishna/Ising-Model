# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:08:39 2023

@author: ashiklalkrishna
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import sys
s_time=time.time()
plt.figure(dpi=200)


def initial(N):
    rand_grid=np.random.random(size=(N,N))
    ini_grid=np.zeros((N, N))
    ini_grid[rand_grid>=frac] = 1
    ini_grid[rand_grid<frac] = -1
    return ini_grid

def flip(grid, t, J, N):        
  for a in range(0,N):
    for b in range(0,N):
      i=np.random.randint(0,N)  
      j=np.random.randint(0,N)
      s=grid[i,j]   
           
      nn=grid [(i+1)%N,j]+ grid [(i-1)%N,j]+grid [i, (j+1)%N]+grid [i, (j-1)%N]
      s_flip=-1*s                
      de = 2*J*s*nn
      
      if de<=0:
        s=s_flip
      elif np.random.random()<np.exp(-de/t):
        s=s_flip
        
      grid[i,j]=s
  return grid

def energy_func(grid,N):
    e=0
    for a in range(0,N):
      for b in range(0,N):
          i=np.random.randint(0,N)  
          j=np.random.randint(0,N)
          s=grid[i,j]   
               
          nn=grid [(i+1)%N,j]+ grid [(i-1)%N,j]+grid [i, (j+1)%N]+grid [i, (j-1)%N]
          e+=-s*nn
    return e/2

frac=0.25
J=1
steps=1000
eqsteps=200
size=[2,4,6,8]
T=np.linspace(0.5,5,30)


for N in size:
    grid=initial(N)
    energy=[]
    for t in T:
        E=0
        for k in range(eqsteps):
            flip(grid, t, J, N)
        for i in range(steps):
            flip(grid, t, J, N)
            e=energy_func(grid, N)
            E+=e
        E_mean=E/steps   
        En=E_mean/(N**2)         
        energy.append(En)
    plt.plot(T,energy,label=f'N={N}')
    
plt.xlabel('Temperature ($J/k_b$)')
plt.ylabel('Average Energy per Spin')
plt.title('Average Energy vs Temperature')
plt.legend()
plt.grid()
plt.show()

f_time=time.time()
e_time=f_time-s_time
print(f'Execution time: {e_time:.2f} seconds')