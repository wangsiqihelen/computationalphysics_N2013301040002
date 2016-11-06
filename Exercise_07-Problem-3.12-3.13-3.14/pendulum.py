import pylab as pl
import numpy as np
import math

class pendulum:
    def __init__(self, initial_omega=0, initial_theta1=0.2, g=9.8, length_of_string=9.8, q=0.5, time_step=0.04,\
                 FD=1.2, OmegaD=2.0/3.0, stepsnumber=15000):
        self.omega1 = [initial_omega]
        self.theta1 = [initial_theta1]
        self.omega2 = [initial_omega]
        self.theta2 = [initial_theta1+0.001]
        self.t = [0]
        self.dt = time_step
        self.g = g
        self.l = length_of_string
        self.q = q
        self.FD = FD
        self.OmegaD = OmegaD
	self.nsteps= stepsnumber
	self.delta_theta = [abs(self.theta2[0]-self.theta1[0])] 

    def run(self):
        for i in range(self.nsteps):
        	self.omega1.append( self.omega1[i] - ( (self.g / self.l) * math.sin( self.theta1[i] ) - self.q * self.omega1[i]+\
self.FD * math.sin(self.OmegaD * self.t[i]) )*self.dt)
        	self.theta1.append( self.theta1[i] + self.omega1[i+1] * self.dt)


        	self.omega2.append( self.omega2[i] - ( (self.g / self.l) * math.sin( self.theta2[i] ) - self.q * self.omega2[i]+\
self.FD * math.sin(self.OmegaD * self.t[i]) )*self.dt)
        	self.theta2.append( self.theta2[i] + self.omega2[i+1] * self.dt)


		self.delta_theta.append( abs(self.theta2[i+1]-self.theta1[i+1]) )

        	self.t.append(self.t[i]+self.dt)

		while self.delta_theta[i] > math.pi :
			self.delta_theta[i] = self.delta_theta[i] - 2*math.pi


    def show_results(self):
        pl.plot(self.t, self.delta_theta,'r')
        pl.xlabel('time ($s$)')
        pl.ylabel('$\Delta \\theta $(radius)')
        pl.show()



a = pendulum()
a.run()
a.show_results()
