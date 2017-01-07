#initial set up
length=1.
N=100000.
dx=length/N


energy=[1.]
delta_energy=0.1
b=2.
judge_e=0.0001
last_diverge = 0.

while abs(delta_energy)>judge_e:
    wave = [1., 1.]
    x = [0.]
    tmp_e=1.

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
    if wave[-1]*last_diverge<0:
        delta_energy=-delta_energy/2.
    tmp_e=energy[-1]+delta_energy
    last_diverge=wave[-1]
    energy.append(tmp_e)
    print(delta_energy)

print(energy[-1])
