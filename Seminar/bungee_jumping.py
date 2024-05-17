import numpy as np
import matplotlib.pyplot as plt

class Bungee:
    def __init__(self,k,l,m,h,e=0,g=9.81):
        self.k=k  #konstanta rastezljivosti
        self.m=m  #masa osobe
        self.ei=e  #ekstenzija uzeta
        self.l=l  #duljina uzeta
        self.hi=h  #visina s koje osoba skace
        self.g=g  

    def motion(self,dt,vrijeme,type='o'):
        self.type=type
        self.vrijeme=vrijeme
        self.dt=dt
        self.lista_t=[]
        self.lista_x=[]
        self.lista_v=[]
        self.lista_Ep=[]
        self.lista_Ek=[]
        self.lista_Eel=[]
        self.lista_h=[self.hi]
        self.lista_ekstenzija=[self.ei]
        for self.t in np.arange(0,self.vrijeme,self.dt):
            if self.t==0:
                self.lista_x.append(0)
                self.lista_v.append(0)
                self.lista_t.append(self.t)
                self.lista_Ep.append(self.m*self.g*self.hi)
                self.lista_Ek.append(0.5*self.m*(self.lista_v[0]**2))
                self.lista_Eel.append(0.5*self.k*(self.lista_ekstenzija[0]**2))
            else:
                self.lista_t.append(self.t)
                self.v=self.lista_v[-1]-self.g*self.dt+((self.k*self.lista_ekstenzija[-1])/self.m)*dt
                self.x=self.lista_x[-1]+self.v*self.dt
                self.h=abs(self.lista_h[-1]+self.x)
                self.e=abs(self.x)-self.l
                self.Ep=self.m*self.g*self.h
                self.Ek=0.5*self.m*(self.v**2)
                self.Eel=0.5*self.k*(self.lista_ekstenzija[-1]**2)
                if self.e > 0:
                    self.lista_ekstenzija.append(self.e)
                else:
                    self.lista_ekstenzija.append(0)
                self.lista_v.append(self.v)
                self.lista_x.append(self.x)
                self.lista_h.append(self.h)
                self.lista_Ep.append(self.Ep)
                self.lista_Ek.append(self.Ek)
                self.lista_Eel.append(self.Eel)
                
        print(self.lista_h)
        print(self.lista_Ep[0],self.lista_Ep[1])
        plt.plot(self.lista_t,self.lista_x)
        plt.show()
        plt.plot(self.lista_t,self.lista_Ep,label='Ep graf')
        plt.plot(self.lista_t,self.lista_Ek,label='Ek graf')
        plt.plot(self.lista_t,self.lista_Eel,label='Eel graf')
        plt.legend()
        plt.show()


b1=Bungee(1,15,70,40)
b1.motion(0.5,60)

        