import matplotlib.pyplot as plt
import numpy as np

#initial set up
length=1.
N=200.
dx=length/N

energy_state=[]
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
        x = [0.]
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
    energy_state.append(energy[-1])
    bigloop=bigloop+1

level=[1.,2.,3.,4.,5.,6.]
level_t=np.arange(0.,7.,0.001)
energy_state_t=[]
for item in level_t:
    energy_state_t.append((item ** 2) * (np.pi ** 2) / 8)

variation=((np.pi ** 2) / 8)-energy_state[0]
gstate=(np.pi ** 2)/8
print(energy_state[0])
#plt.plot(level,energy_state,'ro', level, energy_state_t,'bo')
#plt.show()
step_d=[0.05,0.01,0.005]
var=[1.17373046875,1.22138671875,1.22763671875]
const_line=[gstate,gstate]
xline=[0.,0.06]
lines1,= plt.plot(step_d, var, 'ro',label='Numerical Value')
lines2,= plt.plot(xline, const_line, 'b-',label='Theoretical Ground State')
plt.title('Variation from Theoretical Ground State Energy vs $\Delta x$')
plt.ylabel('Energy')
plt.xlabel('$\Delta x$')
plt.xlim(0.,0.06)
plt.legend(loc=3)
plt.savefig('energy_step.png')
plt.show()