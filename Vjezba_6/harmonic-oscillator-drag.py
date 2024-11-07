import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal



class HarmonicOscillator:
    def __init__(self,k,m,x0=0,v0=0,c1=0.3,c2=0.1):
        self.k=k
        self.m=m
        self.x0=x0
        self.v0=v0
        self.c1=c1
        self.c2=c2
        
        

    def motion(self,dt,vrijeme,c_2='da',type='o'):
        self.c_2=c_2
        if self.c_2=='da':
            self.a0=(-self.c1*(self.v0)-self.c2*(self.v0**2)-self.k*self.x0)/self.m
        else:
            self.a0=(-self.c1*(self.v0)-self.k*self.x0)/self.m
        self.type=type
        self.vrijeme=vrijeme
        self.dt=dt
        self.lista_t=[]
        self.lista_x=[]
        self.lista_v=[]
        self.lista_a=[]
        
        if self.dt<=0.001:
            self.marker=1
        elif self.dt<=0.01:
            self.marker=2
        else:
            self.marker=3

        #self.lista_x.append(self.x0)
        #self.lista_v.append(self.v0)
        if self.c_2=='da':
            for self.t in np.arange(0,self.vrijeme,self.dt):
            #self.lista_t.append(self.t)
                if self.t==0:
                    self.lista_x.append(self.x0)
                    self.lista_v.append(self.v0)
                    self.lista_t.append(self.t)
                else:
                    self.lista_t.append(self.t)
                    self.lista_a.append((-self.c1*(self.lista_v[-1])-self.c2*(self.lista_v[-1]**2)-self.k*self.lista_x[-1])/self.m)
                    self.lista_v.append(self.lista_v[-1]+self.lista_a[-1]*self.dt)
                    self.lista_x.append(self.lista_x[-1]+self.lista_v[-1]*self.dt)
            self.lista_a.append((-self.c1*(self.lista_v[-1])-self.c2*(self.lista_v[-1]**2)-self.k*self.lista_x[-1])/self.m)
        else:
            for self.t in np.arange(0,self.vrijeme,self.dt):
            #self.lista_t.append(self.t)
                if self.t==0:
                    self.lista_x.append(self.x0)
                    self.lista_v.append(self.v0)
                    self.lista_t.append(self.t)
                else:
                    self.lista_t.append(self.t)
                    self.lista_a.append((-self.c1*(self.lista_v[-1])-self.k*self.lista_x[-1])/self.m)
                    self.lista_v.append(self.lista_v[-1]+self.lista_a[-1]*self.dt)
                    self.lista_x.append(self.lista_x[-1]+self.lista_v[-1]*self.dt)
            self.lista_a.append((-self.c1*(self.lista_v[-1])-self.k*self.lista_x[-1])/self.m)
        #print(self.lista_t)
        #print(self.lista_x)
        plt.subplot(3,1,1)
        plt.plot(self.lista_t,self.lista_x,self.type,markersize=self.marker,label='dt = {}'.format(str(self.dt)))
        plt.title('x-t graf')
        plt.xlabel('t [s]')
        plt.ylabel('x [m]')
        plt.xticks(np.arange(0,self.vrijeme,step=0.25))
        plt.yticks(np.arange(-self.x0,self.x0+0.1,step=0.1))
        plt.legend()
        plt.tight_layout()
        plt.subplot(3,1,2)
        plt.plot(self.lista_t,self.lista_v,self.type,markersize=self.marker,label='dt = {}'.format(str(self.dt)))
        plt.title('v-t graf')
        plt.xlabel('t [s]')
        plt.ylabel('v [m/s]')
        plt.xticks(np.arange(0,self.vrijeme,step=0.25))
        plt.yticks(np.arange(round(min(self.lista_v)),(-round(min(self.lista_v)))+1,step=1))
        plt.tight_layout()
        plt.legend()
        plt.subplot(3,1,3)
        plt.plot(self.lista_t,self.lista_a,self.type,markersize=self.marker,label='dt = {}'.format((self.c_2)))
        plt.title('a-t graf')
        plt.xlabel('t [s]')
        plt.ylabel('a [m/s^2]')
        plt.xticks(np.arange(0,self.vrijeme,step=0.25))
        plt.yticks(np.arange(round(min(self.lista_a)),(-round(min(self.lista_a)))+10,step=10))
        plt.tight_layout()
        plt.legend()
        #print(str(self.dt))
        #print(min(self.lista_v))
        
        


    def show(self):
        plt.show()



h1=HarmonicOscillator(10,0.1,0.5,0)
h1.motion(0.05,2,'ne')
h1.motion(0.05,2,'da')
h1.show()

        