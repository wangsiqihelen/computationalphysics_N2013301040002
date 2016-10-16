import pylab as pl
import numpy as np
class cannon_shell:
    def __init__(self, initial_x=0, initial_y=0, g=9.8, time_step=0.01,\
                 initial_x_velocity=50,initial_y_velocity=20):
        self.vx = [initial_x_velocity]
        self.vy = [initial_y_velocity]
        self.x = [initial_x]
        self.y = [initial_y]
        self.t = [0]
        self.dt = time_step
        self.time = 2*initial_y_velocity/g 
	self.g = g
	self.nsteps= 1 + int((2*initial_y_velocity/g) / time_step )
    def run(self):
        for i in range(self.nsteps):
		self.x.append(self.x[i]+self.vx[i]*self.dt)
		self.y.append(self.y[i]+self.vy[i]*self.dt)
		self.vy.append(self.vy[i]- self.g*self.dt)
		self.vx.append(self.vx[i])
		self.t.append(self.dt)
 
    def show_results(self):
	font = {'family': 'serif',
        	'color':  'darkred',
        	'weight': 'normal',
        	'size': 16,
        	}

	pl.plot(self.x, self.y,'k')
        pl.title('Shell trajectories without air resistance', fontdict=font)
        pl.xlabel('x/m', fontdict=font)
        pl.ylabel('y/m', fontdict=font)
	pl.xlim(0.0, 250)
	pl.ylim(0.0, 25)
	pl.text( 140 , 23, \
		'initial_x_velocity=50m/s ',
		  fontdict = font)
	pl.text( 140 , 21, \
		'initial_y_velocity=20m/s',
		  fontdict = font)
	pl.text( 140 , 19, \
		'g=9.8m/s^2',
		  fontdict = font)
        pl.show()

a = cannon_shell()
a.run()
a.show_results() 
