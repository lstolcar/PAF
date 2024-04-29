import numpy as np
import matplotlib.pyplot as plt


class Projectile:
    def __init__(self,t,m,x0,y0,v0,kut,rho,C,A,dt):
        self.t=t
        self.m=m
        self.x0=x0
        self.y0=y0
        self.v0=v0
        self.kut=kut*(np.pi/180)
        self.v0x=self.v0*np.cos(self.kut)
        self.v0y=self.v0*np.sin(self.kut)
        self.rho=rho
        self.C=C
        self.A=A
        self.dt=dt
        self.g=9.81
        self.ax0=-np.sign(self.v0x)*((self.rho*self.C*self.A)/(2*self.m))*(self.v0x)**2
        self.ay0=-self.g-np.sign(self.v0y)*((self.rho*self.C*self.A)/(2*self.m))*(self.v0y)**2

    def euler(self,dt):
        self.dt=dt
        self.lista_ax=[]
        self.lista_vx=[]
        self.lista_x=[]
        self.lista_ay=[]
        self.lista_vy=[]
        self.lista_y=[]
        self.lista_ax.append(self.ax0)
        self.lista_vx.append(self.v0x)
        self.lista_x.append(self.x0)
        self.lista_ay.append(self.ay0)
        self.lista_vy.append(self.v0y)
        self.lista_y.append(self.y0)
        for self.i in np.arange(0,self.t,self.dt):
            self.vx=self.lista_vx[-1]+self.lista_ax[-1]*self.dt
            self.lista_vx.append(self.vx)
            self.vy=self.lista_vy[-1]+self.lista_ay[-1]*self.dt
            self.lista_vy.append(self.vy)
            self.x=self.lista_x[-1]+self.lista_vx[-1]*self.dt
            self.lista_x.append(self.x)
            self.y=self.lista_y[-1]+self.lista_vy[-1]*self.dt
            self.lista_y.append(self.y)
            self.ax=-np.sign(self.lista_vx[-1])*((self.rho*self.C*self.A)/(2*self.m))*(self.lista_vx[-1])**2
            self.lista_ax.append(self.ax)
            self.ay=-self.g-np.sign(self.lista_vy[-1])*((self.rho*self.C*self.A)/(2*self.m))*(self.lista_vy[-1])**2
            self.lista_ay.append(self.ay)
        plt.plot(self.lista_x,self.lista_y)

    
    def Runge_Kutta(self,dt):
        self.dt=dt
        self.lista_vx_kutta=[]
        self.lista_x_kutta=[]
        self.lista_vy_kutta=[]
        self.lista_y_kutta=[]
        self.lista_vx_kutta.append(self.v0x)
        self.lista_x_kutta.append(self.x0)
        self.lista_vy_kutta.append(self.v0y)
        self.lista_y_kutta.append(self.y0)
        self.T=0
        for self.i in np.arange(0,self.t,self.dt):
            self.k1vx=-np.sign(self.lista_vx_kutta[-1])*((self.rho*self.C*self.A)/(2*self.m))*((self.lista_vx_kutta[-1])**2)*self.dt
            self.k1x=self.lista_vx_kutta[-1]*self.dt
            self.k2vx=-np.sign(self.lista_vx_kutta[-1]-((self.k1vx)/2))*((self.rho*self.C*self.A)/(2*self.m))*((self.lista_vx_kutta[-1]+((self.k1vx)/2))**2)*self.dt
            self.k2x=(self.v0x+((self.k2vx)/2))*self.dt
    
    
    
    
    
    
    
    
    
    
    
    
    def plot(self):
        plt.show()





h1=Projectile(2,2,3,15,15,45,1,0,3,0.1)
h1.euler(0.1)
h1.euler(0.01)
h1.euler(0.001)
h1.plot()

