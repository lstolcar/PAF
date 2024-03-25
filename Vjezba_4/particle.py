import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init__(self,v_0,kut,x_0,y_0):
        self.v_0 = v_0
        kut=np.radians(kut)
        self.kut = kut
        self.x_0 = x_0
        self.y_0 = y_0
        self.ax=0
        self.ay=-9.81 
    def reset(self):
         self.v_0 = 0
         self.kut = 0
         self.x_0 = 0
         self.y_0 = 0

    def __move(self,dt):
            self.dt = dt
            self.vx0=self.v_0*np.cos(self.kut)
            self.vy0=self.v_0*np.sin(self.kut)
            self.vx=self.vx0+self.ax*self.dt
            self.vy=self.vy0+self.ay*self.dt
            self.x=self.x_0+self.vx*self.dt
            self.y=self.y_0+self.vy*self.dt
            

    def range(self,dt=0.01):
         self.dt = dt
         self.__move(self.dt)
         self.dt = dt
         self.lista_x=[]
         self.lista_y=[]
         self.lista_vx=[]
         self.lista_vy=[]
         self.lista_x.append(self.x_0)
         self.lista_y.append(self.y_0)
         self.lista_vx.append(self.vx0)
         self.lista_vy.append(self.vy0)
         #print(self.lista_x,self.lista_y,self.lista_vx,self.lista_vy)
         while self.lista_y[-1] >= 0:
              self.lista_vx.append(self.lista_vx[-1])
              self.lista_x.append(self.lista_x[-1]+self.lista_vx[-1]*self.dt)
              self.lista_vy.append(self.lista_vy[-1]+self.ay*self.dt)
              self.lista_y.append(self.lista_y[-1]+self.lista_vy[-1]*self.dt)
              #print(self.lista_x,self.lista_y,self.lista_vx,self.lista_vy)
         self.D_n = self.lista_x[-1]-self.x_0
         #print(self.D_n)
        
    def plot_trajectory(self):
        plt.title('Graf dometa')
        plt.xlabel('x-koordinata[m]')
        plt.ylabel('y-koordinata[m]')
        plt.xticks(np.arange(0,self.lista_x[-1],step=1.5))
        plt.yticks()
        plt.grid()
        plt.plot(self.lista_x,self.lista_y,'r')
        plt.show()
    def domet(self):
        self.D_a=(((self.v_0)**2)/(-self.ay))*np.sin(2*self.kut)
        print(self.D_a)
    def razlika(self):
        self.Error=self.D_a-self.D_n
        print(self.Error)

              

         
         




#p1=Particle(10,45,0,0)
#p1.range(0.01)
#p1.plot_trajectory()
#p1.domet()  
#p1.razlika()     