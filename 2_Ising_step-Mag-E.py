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
plt.figure(figsize=(8,10), dpi=200)


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

def energy_func(grid):
    e=0
    for a in range(0,N):
      for b in range(0,N):
          i=np.random.randint(0,N)  
          j=np.random.randint(0,N)
          s=grid[i,j]   
               
          nn=grid [(i+1)%N,j]+ grid [(i-1)%N,j]+grid [i, (j+1)%N]+grid [i, (j-1)%N]
          e+=-s*nn
    return e/2


frac=0.75
N=50
t=3.5
J=1
steps=1000
#size=[10,20,50,1'00]

grid=initial(N)
mag=[]
energy=[]
timesteps=[]
for i in range(steps):
  flip(grid, t, J, N)
  mag.append(np.sum(grid)/N**2)
  energy.append(energy_func(grid))
  timesteps.append(i)
  
plt.subplot(211)
plt.plot(timesteps,mag, color='teal')
plt.xlabel('Time steps')
plt.ylabel('Magnetization per spin')
plt.title(f'Magnetisation per spin vs Temperature (T={t}, N={N})')
plt.grid()
  
plt.subplot(212)
plt.plot(timesteps,energy,color='red')
plt.xlabel('Time steps')
plt.ylabel('Energy')
plt.title(f'Energy vs Temperature (T={t}, N={N})')
plt.grid()
plt.tight_layout()
plt.show()


'''for N in size:
  grid=initial(N)
  mag=[]
  energy=[]
  timesteps=[]
  for i in range(steps):
    flip(grid, t, J, N)
    mag.append(np.sum(grid)/N**2)
    timesteps.append(i)
  plt.plot(timesteps,mag, label=f'N={N}')
    
plt.xlabel('Time steps')
plt.ylabel('Magnetization per spin')
plt.title(f'Magnetisation per spin vs Temperature (T={t})')
plt.legend()
plt.grid()
plt.show()'''

f_time=time.time()
e_time=f_time-s_time
print(f'Execution time: {e_time:.2f} seconds')