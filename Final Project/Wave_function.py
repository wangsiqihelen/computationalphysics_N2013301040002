import matplotlib.pyplot as plt
import numpy as np

#initial set up
length=1.
N=1000.
dx=length/N

wave_function=[]
bigloop=0
temp_e=[1.,4.,9.,16.,25.,36.]
temp_in=[[1.,1.],[-dx,0.],[1.,1.],[-dx,0.],[1.,1.],[-dx,0.]]
while bigloop<6:
    energy = [temp_e[bigloop]]
    delta_energy = 0.1
    b = 2.
    judge_e = 0.0001
    last_diverge = 0.

    while abs(delta_energy) > judge_e:
        wave = [temp_in[bigloop][0], temp_in[bigloop][1]]
        x = [-dx,0.]
        tmp_e = 1.

        wave_plus = 0.
        x_tmp = 0.
        loop = 0
        while loop < N:
            wave_plus = 2 * wave[-1] - wave[-2] - 2 * (energy[-1]) * (dx ** 2) * wave[-1]
            x_tmp = x[-1] + dx
            if abs(wave_plus) >= b:
                break
            else:
                wave.append(wave_plus)
                x.append(x_tmp)
                loop = loop + 1
        if wave[-1] * last_diverge < 0:
            delta_energy = -delta_energy / 2.
        tmp_e = energy[-1] + delta_energy
        last_diverge = wave[-1]
        energy.append(tmp_e)
        print(delta_energy)
    wave_function.append(wave)
    bigloop=bigloop+1

x_t=np.arange(0.,1.,0.001)
wave_function_t=[]
for item in x_t:
    wave_function_t.append(np.sin(item*(np.pi)*3))

wave_n=[]
for item in wave_function[5]:
    wave_n.append(item*3*np.pi)

lines1,= plt.plot(x, wave_n, 'r-',label='Numerical Value')
lines2,= plt.plot(x_t, wave_function_t, 'b--',label='Theoretical Curve')
plt.title('Numerical vs Theoretical Wave Function for $n=6$')
plt.xlabel('X')
plt.ylabel('Wave Function')
plt.legend()
plt.xlim(0.,1.)
plt.savefig('wave_6.png')
plt.show()