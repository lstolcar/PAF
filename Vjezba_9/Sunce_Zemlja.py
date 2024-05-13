import numpy as np
import matplotlib.pyplot as plt
class tijela:
    def __init__(self,xZ=1.486*(10**11),yZ=0,xS=0,yS=0,mZ=5.9742*(10.**24.),mS=1.989*(10.**30.),vxi=0,vyi=29783.,vSunca=0,godina=365.242,G=6.67408*(10.**(-11.))):
        self.pozicija_iZ=np.array((xZ,yZ))
        self.pozicija_iS=np.array((xS,yS))
        self.vi_Z=np.array((vxi,vyi))
        self.vi_S=np.array((0,vSunca))
        self.godina=godina*86400
        self.G=G
        self.mZ=mZ
        self.mS=mS

    def pomicaj(self,dt=3600):
        self.dt=dt
        self.lista_pozicija_Z=[self.pozicija_iZ]
        self.lista_pozicija_S=[self.pozicija_iS]
        self.lista_vZ=[self.vi_Z]
        self.lista_vS=[self.vi_S]
        self.lista_aZ=[]
        self.lista_aS=[]
        self.T=0
        self.lista_xZ=[self.pozicija_iZ[0]]
        self.lista_yZ=[self.pozicija_iZ[1]]
        self.lista_xS=[self.pozicija_iS[0]]
        self.lista_yS=[self.pozicija_iS[1]]
        #print((np.subtract(self.pozicija_iZ,self.pozicija_iS)))
    
        
        
        

    
        while self.T<self.godina:
            self.aZ=(-self.G*((self.mS)/((abs(np.linalg.norm(np.subtract(self.lista_pozicija_Z[-1],self.lista_pozicija_S[-1])))**3))))*(self.lista_pozicija_Z[-1]-self.lista_pozicija_S[-1])
            self.aS=(-self.G*((self.mZ)/((abs(np.linalg.norm(np.subtract(self.lista_pozicija_S[-1],self.lista_pozicija_Z[-1]))))**3)))*(self.lista_pozicija_S[-1]-self.lista_pozicija_Z[-1])
            self.vZ=self.lista_vZ[-1]+self.aZ*self.dt
            self.pozicija_Z=self.lista_pozicija_Z[-1]+self.vZ*self.dt
            self.vS=self.lista_vS[-1]+self.aS*self.dt
            self.pozicija_S=self.lista_pozicija_S[-1]+self.vS*self.dt
            self.lista_aZ.append(self.aZ)
            self.lista_aS.append(self.aS)
            self.lista_vZ.append(self.vZ)
            self.lista_vS.append(self.vS)
            self.lista_xZ.append(self.pozicija_Z[0])
            self.lista_yZ.append(self.pozicija_Z[1])
            self.lista_xS.append(self.pozicija_S[0])
            self.lista_yS.append(self.pozicija_S[1])
            self.lista_pozicija_S.append(self.pozicija_S)
            self.lista_pozicija_Z.append(self.pozicija_Z)
            
            self.T=self.T+self.dt

        print(self.lista_vZ[0],self.lista_vZ[1])
    def plot(self):
    
        plt.plot(self.lista_xZ,self.lista_yZ,'b',label='Zemlja')

        plt.plot(self.lista_xS,self.lista_yS,'orange',label='Sunce',marker='.',markersize=10)
        plt.axis('square')
        plt.legend()
        plt.show()




















p1=tijela()
p1.pomicaj()
p1.plot()