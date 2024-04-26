import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal



class HarmonicOscillator:
    def __init__(self,k,m,x0=0,v0=0):
        self.k=k
        self.m=m
        self.x0=x0
        self.v0=v0
        self.a0=-(self.k/self.m)*self.x0

    def motion(self,dt,vrijeme,type='o'):
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
        for self.t in np.arange(0,self.vrijeme,self.dt):
            #self.lista_t.append(self.t)
            if self.t==0:
                self.lista_x.append(self.x0)
                self.lista_v.append(self.v0)
                self.lista_t.append(self.t)
            else:
                self.lista_t.append(self.t)
                self.lista_a.append(-(self.k/self.m)*self.lista_x[-1])
                self.lista_v.append(self.lista_v[-1]+self.lista_a[-1]*self.dt)
                self.lista_x.append(self.lista_x[-1]+self.lista_v[-1]*self.dt)
        self.lista_a.append(-(self.k/self.m)*self.lista_x[-1])
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
        plt.plot(self.lista_t,self.lista_a,self.type,markersize=self.marker,label='dt = {}'.format(str(self.dt)))
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
    

    def period(self,d_t,t_):
        self.t_=t_
        self.d_t=d_t
        self.lista_t=[]
        self.lista_x=[]
        self.lista_v=[]
        self.lista_a=[]
        for self.time in np.arange(0,self.t_,self.d_t):
            if self.time==0:
                self.lista_t.append(self.time)
                self.lista_x.append(self.x0)
                self.lista_v.append(self.v0)
                self.lista_t.append(self.time)
            else:
                self.lista_t.append(self.time)
                self.lista_a.append(-(self.k/self.m)*self.lista_x[-1])
                self.lista_v.append(self.lista_v[-1]+self.lista_a[-1]*self.d_t)
                self.lista_x.append(self.lista_x[-1]+self.lista_v[-1]*self.d_t)
        self.lista_a.append(-(self.k/self.m)*self.lista_x[-1])
        self.lista_perioda=[]
        for self.ele in self.lista_x:
            if 0.00001< abs(self.ele-min(self.lista_x)) <0.01:
                self.index=self.lista_x.index(self.ele)
                self.index_min=self.lista_x.index(min(self.lista_x))
                if abs(self.lista_t[self.index]-self.lista_t[self.index_min]) > 0.1:
                    self.lista_perioda.append(abs(self.lista_t[self.index]-self.lista_t[self.index_min]))
                    #print(self.lista_perioda)
                #print((sum(self.lista_perioda))/len(self.lista_perioda))
                #print(min(self.lista_x))
                #print(self.lista_t[self.index])
                #print(self.lista_t[self.index_min])
                #print(self.ele)
                #print(min(self.lista_x))
                #print(self.index)
        #print(self.lista_x)
        #print((sum(self.lista_perioda))/len(self.lista_perioda))
        #print(self.lista_perioda)
        #print(len(self.lista_perioda))
        self.lista_perioda_avr=[]
        if len(self.lista_perioda) <=2:
            self.lista_perioda_avr=self.lista_perioda
        elif len(self.lista_perioda)%2==0:
            for self.i in range(len(self.lista_perioda)/2):
                self.lista_perioda_avr.append(min(self.lista_perioda))
                self.lista_perioda.remove(min(self.lista_perioda))
        elif len(self.lista_perioda)%2 != 0:
            for self.i in range((len(self.lista_perioda)/2)-1):
                self.lista_perioda_avr.append(min(self.lista_perioda))
                self.lista_perioda.remove(min(self.lista_perioda))

        print(np.average(self.lista_perioda_avr))
        print(np.average(self.lista_perioda_avr)-(2*np.pi*np.sqrt(self.m/self.k)))
        #kod je prilicno tocan za sve dt-ove, no pri smanjenju je manje tocan
    def period_1(self,d_t,t_):
        self.t_=t_
        self.d_t=d_t
        self.lista_t=[]
        self.lista_x=[]
        self.lista_v=[]
        self.lista_a=[]
        for self.time in np.arange(0,self.t_,self.d_t):
            if self.time==0:
                self.lista_t.append(self.time)
                self.lista_x.append(self.x0)
                self.lista_v.append(self.v0)
                self.lista_t.append(self.time)
            else:
                self.lista_t.append(self.time)
                self.lista_a.append(-(self.k/self.m)*self.lista_x[-1])
                self.lista_v.append(self.lista_v[-1]+self.lista_a[-1]*self.d_t)
                self.lista_x.append(self.lista_x[-1]+self.lista_v[-1]*self.d_t)
        self.lista_a.append(-(self.k/self.m)*self.lista_x[-1])
        self.lista_tmax=[]
        self.lista_tmin=[]
        #kada prvo raste
        if self.lista_x[1]-self.lista_x[0]>0:
            for self.i in range(1,len(self.lista_x)):
                if self.lista_x[self.i-1]>self.lista_x[self.i]:
                    self.lista_tmax.append(self.i-1)
            for self.y in range(self.lista_tmax[0],len(self.lista_x)):
                if self.lista_x[self.y-1]<self.lista_x[self.y]:
                    self.lista_tmin.append(self.y-1)
        #kada prvo pada
        if self.lista_x[1]-self.lista_x[0]<0:
            for self.i in range(1,len(self.lista_x)):
                if self.lista_x[self.i-1]<self.lista_x[self.i]:
                    self.lista_tmin.append(self.i-1)
                    #print(self.i-1)
            for self.y in range(self.lista_tmin[0],len(self.lista_x)):
                if self.lista_x[self.y-1]>self.lista_x[self.y]:
                    self.lista_tmax.append(self.y-1)
                    #print(self.y-1)
        #print(self.lista_tmax)
        #print(self.lista_tmin)
        print(abs(self.lista_t[self.lista_tmax[1]]-self.lista_t[self.lista_tmin[1]])*2)
        #print(self.lista_t)
        print(abs(self.lista_t[self.lista_tmax[1]]-self.lista_t[self.lista_tmin[1]])*2-(2*np.pi*np.sqrt(self.m/self.k)))
        #ovaj kod je prilicno tocan za male razlike u dt-u

















h1=HarmonicOscillator(10,0.1,0.3,0)
h1.motion(0.05,2)
h1.motion(0.001,2)
h1.motion(0.01,2)
h1.show()
h1.period(0.001,2)
h1.period_1(0.001,2)

