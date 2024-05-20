import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

class Bungee:
    def __init__(self,k,l,m,h,e=0,g=9.81,rho=0.6,C=0.1,A=0.5):
        self.A=A #površina okomita na smjer gibanja
        self.C=C #koeficijent trenja
        self.rho=rho #gustoća zraka
        self.k=k  #konstanta rastezljivosti
        self.m=m  #masa osobe
        self.ei=e  #ekstenzija uzeta
        self.l=l  #duljina uzeta
        self.hi=h  #visina s koje osoba skace
        self.g=g  

    def motion(self,dt,vrijeme,otpor='Ne'):
        self.otpor=otpor
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
        self.lista_ZOE=[]
        if self.otpor=='Ne':
            for self.t in np.arange(0,self.vrijeme,self.dt):
                if self.t==0:
                    self.lista_x.append(0)
                    self.lista_v.append(0)
                    self.lista_t.append(self.t)
                    self.lista_Ep.append(self.m*self.g*self.hi)
                    self.lista_Ek.append(0.5*self.m*(self.lista_v[0]**2))
                    self.lista_Eel.append(0.5*self.k*(self.lista_ekstenzija[0]**2))
                    self.Zoe=self.lista_Ep[0]-(self.lista_Ep[0]+self.lista_Ek[0]+self.lista_Eel[0])
                    self.lista_ZOE.append(self.Zoe)
                else:
                    self.lista_t.append(self.t)
                    self.v=self.lista_v[-1]-self.g*self.dt+((self.k*self.lista_ekstenzija[-1])/self.m)*dt
                    self.x=self.lista_x[-1]+self.v*self.dt
                    self.h=self.lista_h[0]+self.x
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
                    self.Zoe=self.lista_Ep[0]-(self.Ep+self.Ek+self.Eel)
                    #print((self.Ep+self.Ek+self.Eel))
                    self.lista_ZOE.append(self.Zoe)
        else:
             for self.t in np.arange(0,self.vrijeme,self.dt):
                if self.t==0:
                    self.lista_x.append(0)
                    self.lista_v.append(0)
                    self.lista_t.append(self.t)
                    self.lista_Ep.append(self.m*self.g*self.hi)
                    self.lista_Ek.append(0.5*self.m*(self.lista_v[0]**2))
                    self.lista_Eel.append(0.5*self.k*(self.lista_ekstenzija[0]**2))
                    self.Zoe=self.lista_Ep[0]-(self.lista_Ep[0]+self.lista_Ek[0]+self.lista_Eel[0])
                    self.lista_ZOE.append(self.Zoe)
                else:
                    self.ay=-np.sign(self.lista_v[-1])*((self.rho*self.C*self.A)/(2*self.m))*(self.lista_v[-1])**2
                    self.lista_t.append(self.t)
                    self.v=self.lista_v[-1]-self.g*self.dt+((self.k*self.lista_ekstenzija[-1])/self.m)*dt+self.ay*self.dt
                    self.x=self.lista_x[-1]+self.v*self.dt
                    self.h=self.lista_h[0]+self.x
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
                    self.Zoe=self.lista_Ep[0]-(self.Ep+self.Ek+self.Eel)
                    self.a=self.lista_Ep[0]-(self.Ep+self.Ek+self.Eel)
                    self.lista_ZOE.append(self.a)
        #print(np.average(self.lista_ZOE))        
        #print(self.lista_x)
        #print(self.lista_Ep[0],self.lista_Ep[1])
        plt.plot(self.lista_t,self.lista_h)
        plt.xlabel('t [s]')
        plt.ylabel('visina na kojoj se osoba nalazi [m]')
        plt.show()
        plt.plot(self.lista_t,self.lista_Ep,label='Ep graf')
        plt.plot(self.lista_t,self.lista_Ek,label='Ek graf')
        plt.plot(self.lista_t,self.lista_Eel,label='Eel graf')
        plt.xlabel('t [s]')
        plt.ylabel('Iznos energije [J]')
        plt.legend()
        plt.show()


    def animacija(self):
        plt.rcParams['figure.figsize']=[5,5]
        plt.rcParams['figure.autolayout']=True
        fig=plt.figure()
        ax=plt.axes(xlim=(-1,1),ylim=(0,80))

        line,=ax.plot([],[],'o',color='orange')
        line2,=ax.plot([],[],color='black')

        def init():
            line.set_data([],[])
            line2.set_data([],[])

            return line, line2
        def animate(i):
            y=self.lista_h[i]
            line.set_data(0,y)
            line2.set_data(0,[self.lista_h[0],y])

            return line2, line
        
        anim=ani.FuncAnimation(fig,animate,init_func=init,frames=2000,interval=60,blit=True)
        plt.show()

        plt.rcParams['figure.figsize']=[5,5]
        plt.rcParams['figure.autolayout']=True
        fig=plt.figure()
        ax=plt.axes(xlim=(0,60),ylim=(-2000,5000))

        line,=ax.plot([],[],color='blue')

        def init():
            line.set_data([],[])
            

            return line
        def animate(j):
            line.set_data(self.lista_t[:j],self.lista_Ep[:j])

            return line
        
        anim=ani.FuncAnimation(fig,animate,init_func=init,frames=len(self.lista_t),interval=60,blit=True)
        plt.show()



b1=Bungee(100,15,70,80)
b1.motion(0.05,60,'Da')
b1.animacija()

        