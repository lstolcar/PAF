import numpy as np
import matplotlib.pyplot as plt
class planeti:
    def __init__(self,xZ=1,yZ=0,xS=0,yS=0,mZ=5.9742*(10**24),mS=1989*(10**30),vZokomita=29783,vSunca=0,godina=365.242,G=6.67408*(10**(-11))):
        self.polozajZ=np.array((xZ,yZ))
        self.polozajS=np.array((xS,yS))
        self.vZokomita=vZokomita
        self.vSunca=vSunca
        self.godina=godina
        self.G=G
        self.mZ=mZ
        self.mS=mS

    def pomicaj(self,dt=0.25):
        self.dt=dt
        self.lista_aZ=[]
        self.lista_vZ=[]
        self.lista_polozajZ=[]
        self.lista_xZ=[]
        self.lista_yZ=[]
        self.lista_aS=[]
        self.lista_vS=[]
        self.lista_polozajS=[]
        self.lista_xS=[]
        self.lista_yS=[]
        self.T=0
        self.aZi=-self.G*(self.mS/((abs(self.polozajZ-self.polozajS))**3))*(self.polozajZ-self.polozajS)
        self.aSi=-self.G*(self.mZ/((abs(self.polozajS-self.polozajZ))**3))*(self.polozajS-self.polozajZ)
        self.lista_aZ.append(self.aZi)
        self.lista_aS.append(self.aSi)
        self.lista_vZ.append(self.vZokomita)
        self.lista_vS.append(self.vSunca)
        self.lista_polozajZ.append(self.polozajZ)
        self.lista_polozajS.append(self.polozajS)
        self.lista_xZ.append(self.polozajZ[0])
        self.lista_yZ.append(self.polozajZ[1])
        self.lista_xS.append(self.polozajS[0])
        self.lista_yS.append(self.polozajS[1])
        while self.T<self.godina:
            self.vZ=self.lista_vZ[-1]+self.lista_aZ[-1]*self.dt
            self.polozaj_Z=self.lista_polozajZ[-1]+self.vZ*self.dt
            self.vS=self.lista_vS[-1]+self.lista_aS[-1]*self.dt
            self.polozaj_S=self.lista_polozajS[-1]+self.vS*self.dt
            self.aZ=-self.G*(self.mS/((abs(self.polozaj_Z-self.polozaj_S))**3))*(self.polozaj_Z-self.polozaj_S)
            self.aS=-self.G*(self.mZ/((abs(self.polozaj_S-self.polozaj_Z))**3))*(self.polozaj_S-self.polozaj_Z)
            self.lista_aZ.append(self.aZ)
            self.lista_aS.append(self.aS)
            self.lista_vZ.append(self.vZ)
            self.lista_vS.append(self.vS)
            self.lista_polozajZ.append(self.polozaj_Z)
            self.lista_polozajS.append(self.polozaj_S)
            self.lista_xZ.append(self.polozaj_Z[0])
            self.lista_yZ.append(self.polozaj_Z[1])
            self.lista_xS.append(self.polozaj_S[0])
            self.lista_yS.append(self.polozaj_S[1])
            self.T=self.T+self.dt


    def plot(self):
        plt.plot(self.lista_xZ,self.lista_yZ)
        plt.plot(self.lista_xS,self.lista_yS)
        plt.show()




















p1=planeti()
p1.pomicaj()
p1.plot()