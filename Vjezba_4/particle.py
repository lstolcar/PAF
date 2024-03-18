import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init__(self,v_0,kut,x_0,y_0):
        self.v_0 = v_0
        kut=np.radians(kut)
        self.kut = kut
        self.x_0 = x_0
        self.y_0 = y_0
        
    def __move(self,dt):
            self.ax=0
            self.ay=-9.81  
            self.vx0=self.v_0*np.cos(self.kut)
            self.vy0=self.v_0*np.sin(self.kut)
            self.vx=self.vx0+self.ax*dt
            self.vy=self.vy0+self.ay*dt
            self.x=self.x_0+self.vx*dt
            self.y=self.y_0+self.vy*dt
            print(self.x)
            print(self.y)
            print(self.vx)
            print(self.vy)

    def range(self):
         lista_x=[]
         
         




p1=Particle(10,45,3,4)
p1.move(0.01) 
        