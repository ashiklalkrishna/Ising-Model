#modified ising_multi_T_E_C_X

import numpy as np
import matplotlib.pyplot as plt
import numba
from numba import njit
import time

s_time=time.time()
plt.figure(figsize=(8,15))


def initial(N):
    rand_grid=np.random.random(size=(N,N))
    ini_grid=np.zeros((N, N))
    ini_grid[rand_grid>=frac] = 1
    ini_grid[rand_grid<frac] = -1
    return ini_grid


@njit("f8[:,:](f8[:,:], f8, f8, i8)")
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

@njit("f8(f8[:,:],i8)")
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

@njit("f8(f8[:,:])")
def magnetization_func (grid):
    mag=np.sum(grid)
    return mag

frac=0.25
N=100
J=1
steps=1000
eqsteps=200
T=np.linspace(0.5,5,50)
energy=[]
magnetization=[]
specific_heat=[]
susceptibility=[]
    
for t in T:
    grid=initial(N)
    E=0
    M=0
    E_sqr=0
    M_sqr=0
    for k in range(eqsteps):
        flip(grid, t, J, N)
    for i in range(steps):
        flip(grid, t, J, N)
        e=energy_func(grid, N)
        m=magnetization_func(grid)
        E+=e
        M+=m
        E_sqr+=e**2
        M_sqr+=m**2
    E_mean=E/steps
    M_mean=M/steps
    E_sqr_mean=E_sqr/steps
    M_sqr_mean=M_sqr/steps
     
    En=E_mean/(N**2)
    Mag=M_mean/(N**2)
    Cv=(E_sqr_mean-  E_mean**2)/((N**2)*(t**2))
    X=(M_sqr_mean-M_mean**2)/((N**2)*t)
     
    energy.append(En)
    magnetization.append(Mag)
    specific_heat.append(Cv)
    susceptibility.append(X)
#data=pd.DataFrame({'T':T,'E':energy,'M':magnetizatio,'Cv':specific_heat,'X':susceptibility})
#data.to_csv('data.csv',index=False)

plt.subplot(411)
plt.plot(T,energy,color='orangered', marker='.')
plt.xlabel('Temperature ($J/k_b$)')
plt.ylabel('Average Energy per Spin')
plt.title(f'Average Energy vs Temperature (N={N})')
plt.grid()


plt.subplot(412)
plt.plot(T,magnetization,color='teal', marker='.')
plt.xlabel('Temperature ($J/k_b$)')
plt.ylabel('Average Magnetization per spin')
plt.title(f'Average Magnetization vs Temperature (N={N})')
plt.grid()


plt.subplot(413)
plt.plot(T,specific_heat,color='maroon', marker='.')
plt.xlabel('Temperature ($J/k_b$)')
plt.ylabel('Specific heat')
plt.title(f'Specific heat vs Temperature (N={N})')
plt.grid()


plt.subplot(414)
plt.plot(T,susceptibility,color='darkblue', marker='.')
plt.xlabel('Temperature ($J/k_b$)')
plt.ylabel('Susceptibility')
plt.title(f'Susceptibility vs Temparature (N={N})')
plt.grid()
plt.tight_layout()

f_time=time.time()
e_time=f_time-s_time
print(f'Execution time: {e_time:.2f} seconds')