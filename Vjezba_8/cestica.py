import numpy as np
import matplotlib.pyplot as plt
import pdb

print("A")
#pdb.set_trace()

class Cestica:
    #pdb.set_trace()
    def __init__(self,m=1,q=1,vxi=0.1,vyi=0.1,vzi=0.1,Bx=0,By=0,Bz=1,Ex=0,Ey=0,Ez=0,x=0,y=0,z=0,dt=0.01,ti=0,t=5):
        self.m=m
        self.qp=q
        self.qn=-q
        self.vi=np.array((vxi,vyi,vzi))
        self.B=np.array((Bx,By,Bz))
        self.E=np.array((Ex,Ey,Ez))
        self.xi=np.array((x,y,z))
        self.dt=dt
        self.ti=ti
        self.t=t
        self.aip=(self.qp*(self.E+np.cross(self.vi,self.B)))/self.m
        self.ain=(self.qn*(self.E+np.cross(self.vi,self.B)))/self.m
        

    #pdb.set_trace()

    def putanja(self):
        self.lista_qp=[(0,0,0)]
        self.lista_qn=[(0,0,0)]
        #pdb.set_trace()
        #self.lista_px=[0]
        #self.lista_py=[0]
        #self.lista_pz=[0]
        #self.lista_nx=[0]
        #self.lista_ny=[0]
        #self.lista_nz=[0]
        self.lista_ap=[]
        self.lista_vp=[]
        self.lista_an=[]
        self.lista_vn=[]
        self.lista_t=[]
        print("5")
        self.lista_t.append(self.dt)
        self.lista_ap.append(self.aip)
        self.lista_vp.append(self.vi)
        self.lista_an.append(self.ain)
        self.lista_vn.append(self.vi)
        self.T=0
        while self.T<self.t:
            self.ap=(self.qp*(self.E+np.cross(self.lista_vp[-1],self.B)))/self.m
            self.an=(self.qn*(self.E+np.cross(self.lista_vn[-1],self.B)))/self.m
            self.vp=self.lista_vp[-1]+self.ap*self.dt
            self.vn=self.lista_vn[-1]+self.an*self.dt
            self.xp=self.lista_qp[-1]+self.vp*self.dt
            self.xn=self.lista_qn[-1]+self.vn*self.dt
            self.lista_ap.append(self.ap)
            self.lista_an.append(self.an)
            self.lista_vp.append(self.vp)
            self.lista_vn.append(self.vn)
            self.lista_qp.append(self.xp)
            self.lista_qn.append(self.xn)
            self.T=self.T+self.dt
        #print(self.lista_qp)
            






c1=Cestica(1,1,0.1,0.1,0.1,0,0,1,0,0,0,0,0,0,0.01,0,5)
#pdb.set_trace()
c1.putanja()