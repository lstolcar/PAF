import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init__(self,v_0,kut,x_0,y_0):
        self.v_0 = v_0
        kut=np.radians(kut)
        self.kut = kut
        self.x_0 = x_0
        self.y_0 = y_0
    def reset(self):
         self.v_0 = 0
         self.kut = 0
         self.x_0 = 0
         self.y_0 = 0

    def __move(self,dt):
            self.dt = dt
            self.ax=0
            self.ay=-9.81  
            self.vx0=self.v_0*np.cos(self.kut)
            self.vy0=self.v_0*np.sin(self.kut)
            self.vx=self.vx0+self.ax*self.dt
            self.vy=self.vy0+self.ay*self.dt
            self.x=self.x_0+self.vx*self.dt
            self.y=self.y_0+self.vy*self.dt
            

    def range(self):
         self.__move(0.01)
         self.lista_x=[]
         self.lista_y=[]
         self.lista_vx=[]
         self.lista_vy=[]
         self.lista_x.append(self.x_0)
         self.lista_y.append(self.y_0)
         self.lista_vx.append(self.vx0)
         self.lista_vy.append(self.vy0)
         print(self.lista_x,self.lista_y,self.lista_vx,self.lista_vy)
         while self.lista_y[-1] >= 0:
              self.lista_vx.append(self.lista_vx[-1])
              self.lista_x.append(self.lista_x[-1]+self.lista_vx[-1]*self.dt)
              self.lista_vy.append(self.lista_vy[-1]+self.ay*self.dt)
              self.lista_y.append(self.lista_y[-1]+self.lista_vy[-1]*self.dt)
              #print(self.lista_x,self.lista_y,self.lista_vx,self.lista_vy)
         self.D = self.lista_x[-1]-self.x_0
         print(self.D)
        
    def plot_trajectory(self):
        plt.title('Graf dometa')
        plt.xlabel('x-koordinata[m]')
        plt.ylabel('y-koordinata[m]')
        plt.xticks(np.arange(0,self.lista_x[-1],step=1.5))
        plt.yticks()
        plt.grid()
        plt.plot(self.lista_x,self.lista_y,'r')
        plt.show()

              

         
         




p1=Particle(10,45,3,4)
p1.range()
p1.plot_trajectory()
        