import pylab as pl
import numpy as np

number_of_nuclei_A = 100
number_of_nuclei_B = 0
time_constant_A = 1
time_constant_B = 1
time_of_duration = 5
time_step = 0.05
# unit of time is second
        
n_uranium_A = [number_of_nuclei_A]
n_uranium_B = [number_of_nuclei_B]
t = [0]
tau_A = time_constant_A
tau_B = time_constant_B
dt = time_step
time = time_of_duration
nsteps = int(time_of_duration // time_step + 1)

print("Initial number of nuclei A ->", number_of_nuclei_A)
print("Initial number of nuclei B ->", number_of_nuclei_B)
print("Time constant_A ->", time_constant_A)
print("Time constant_B ->", time_constant_B)
print("time step -> ", time_step)
print("total time -> ", time_of_duration)
    

for i in range(nsteps):
            tmp_A = n_uranium_A[i] + ((n_uranium_B[i] - n_uranium_A[i]) / tau_A) * dt

            tmp_B = n_uranium_B[i] + ((n_uranium_A[i] - n_uranium_B[i]) / tau_B) * dt
            t.append(t[i] + dt)
            n_uranium_A.append(tmp_A)
            n_uranium_B.append(tmp_B)

def show_results():
        plot1, = pl.plot(t, n_uranium_A,'r')
        plot2, = pl.plot(t, n_uranium_B,'g')
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
	pl.show()
        
show_results()
