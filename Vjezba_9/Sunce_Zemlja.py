import numpy as np
import matplotlib.pyplot as plt
class tijela:
    def __init__(self,xZ=1.486*(10**11),yZ=0,xS=0,yS=0,mZ=5.9742*(10**24),mS=1989*(10**30),vxi=0,vyi=29783,vSunca=0,godina=365.242,G=6.67408*(10**(-11))):
        self.xZi=xZ
        self.yZi=yZ
        self.xSi=xS
        self.ySi=yS
        self.vxi=vxi
        self.vyi=vyi
        self.vSunca=vSunca
        self.godina=godina*86400
        self.G=G
        self.mZ=mZ
        self.mS=mS

    def pomicaj(self,dt=0.05):
        self.dt=dt*86400
        self.lista_xZ=[self.xZi]
        self.lista_yZ=[self.yZi]
        self.lista_xS=[self.xSi]
        self.lista_yS=[self.ySi]
        self.lista_vxZ=[self.vxi]
        self.lista_vyZ=[self.vyi]
        self.lista_vxS=[0]
        self.lista_vyS=[0]
        self.lista_axZ=[]
        self.lista_ayZ=[]
        self.lista_axS=[]
        self.lista_ayS=[]
        self.axZi=-self.G*((self.mS)/((abs(np.sqrt(((self.xZi-self.xSi)**2)+(self.yZi-self.ySi)**2))))**3)*(np.sqrt(((self.xZi-self.xSi)**2)+(self.yZi-self.ySi)**2))
        self.ayZi=-self.G*((self.mS)/((abs(np.sqrt(((self.xZi-self.xSi)**2)+(self.yZi-self.ySi)**2))))**3)*(np.sqrt(((self.xZi-self.xSi)**2)+(self.yZi-self.ySi)**2))
        self.axSi=-self.G*((self.mZ)/((abs(np.sqrt(((self.xZi-self.xSi)**2)+(self.yZi-self.ySi)**2))))**3)*self.xSi
        self.aySi=-self.G*((self.mZ)/((abs(np.sqrt(((self.xZi-self.xSi)**2)+(self.yZi-self.ySi)**2))))**3)*self.ySi
        self.lista_axZ.append(self.axZi)
        self.lista_ayZ.append(self.ayZi)
        self.lista_axS.append(self.axSi)
        self.lista_ayS.append(self.aySi)
        self.T=0
        
        

    
        while self.T<self.godina:
            self.vxZ=self.lista_vxZ[-1]+self.lista_axZ[-1]*self.dt
            self.vyZ=self.lista_vyZ[-1]+self.lista_ayZ[-1]*self.dt
            #print(self.vxZ)
            #print(self.vyZ)
            self.xZ=self.lista_xZ[-1]+self.vxZ*self.dt
            self.yZ=self.lista_yZ[-1]+self.vyZ*self.dt
            #print(self.xZ)
            #print(self.yZ)
            self.vxS=self.lista_vxS[-1]+self.lista_axS[-1]*self.dt
            self.vyS=self.lista_vyS[-1]+self.lista_ayS[-1]*self.dt
            self.xS=self.lista_xS[-1]+self.vxS*self.dt
            self.yS=self.lista_yS[-1]+self.vyS*self.dt
            self.axZ=-self.G*((self.mS)/((abs(np.sqrt(((self.xZ-self.xS)**2)+(self.yZ-self.yS)**2))))**3)*(self.xZ-self.xS)
            self.ayZ=-self.G*((self.mS)/((abs(np.sqrt(((self.xZ-self.xS)**2)+(self.yZ-self.yS)**2))))**3)*(self.yZ-self.yS)
            #print(self.ayZ)
            self.axS=-self.G*((self.mZ)/((abs(np.sqrt(((self.xZ-self.xS)**2)+(self.yZ-self.yS)**2))))**3)*(self.xS-self.xZ)
            self.ayS=-self.G*((self.mZ)/((abs(np.sqrt(((self.xZ-self.xS)**2)+(self.yZ-self.yS)**2))))**3)*(self.yS-self.yZ)
            self.lista_axZ.append(self.axZ)
            self.lista_ayZ.append(self.ayZ)
            self.lista_axS.append(self.axS)
            self.lista_ayS.append(self.ayS)
            self.lista_vxZ.append(self.vxZ)
            self.lista_vyZ.append(self.vyZ)
            self.lista_vxS.append(self.vxS)
            self.lista_vyS.append(self.vyS)
            self.lista_xZ.append(self.xZ)
            self.lista_yZ.append(self.yZ)
            self.lista_xS.append(self.xS)
            self.lista_yS.append(self.yS)
            self.T=self.T+self.dt

        #print(self.lista_vZ)
    def plot(self):
        plt.plot(self.lista_xZ,self.lista_yZ)
        plt.plot(self.lista_xS,self.lista_yS)
        plt.show()




















p1=tijela()
p1.pomicaj()
p1.plot()