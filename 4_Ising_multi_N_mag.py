# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:08:39 2023

@author: ashiklalkrishna
"""
#Absolute magnetsation per spin vs Temperature

import numpy as np
import matplotlib.pyplot as plt
#import numba
#from numba import njit
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

#@njit("f8[:,:](f8[:,:], f8, f8, i8)")
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

def magnetization_func (grid):
    mag=np.sum(grid)
    return mag

frac=0.25
J=1
steps=1000000
eqsteps=1000
size=[2,4,6,8]
T=np.linspace(0.5,5,30)
markers = ['.', 'o', '^', 's']

for N in size:
   grid=initial(N)
   magnetization=[]
   for t in T:
       M=0
       for k in range(eqsteps):
          flip(grid, t, J, N)
       for i in range(steps):
          flip(grid, t, J, N)
          mag=np.sum(grid)
          M+=abs(mag)
       M_mean=M/steps
       Mag=M_mean/(N**2)
       magnetization.append(Mag)
   plt.plot(T,magnetization, label=f'N={N}', marker ='.')
   
plt.xlabel('Temperature ($J/k_b$)')
plt.ylabel('Absolute Magnetization per spin (<|M|>/N)')
plt.title('Absolute Magnetisation per spin Magnetization vs Temperature')
plt.legend()
plt.grid()
plt.show()

f_time=time.time()
e_time=f_time-s_time
print(f'Execution time: {e_time:.2f} seconds')