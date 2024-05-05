import numpy as np
import matplotlib.pyplot as plt
import pdb
#pdb.set_trace()

class Cestica:
    #pdb.set_trace()
    def __init__(self,m=1,q=1,vxi=0.1,vyi=0.1,vzi=0.1,Bx=0,By=0,Bz=1,Ex=0,Ey=0,Ez=0,x=0,y=0,z=0,dt=0.01,ti=0,t=20):
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
        self.lista_px=[0]
        self.lista_py=[0]
        self.lista_pz=[0]
        self.lista_nx=[0]
        self.lista_ny=[0]
        self.lista_nz=[0]
        self.lista_ap=[]
        self.lista_vp=[]
        self.lista_an=[]
        self.lista_vn=[]
        self.lista_t=[]
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
            self.lista_px.append(self.xp[0])
            self.lista_py.append(self.xp[1])
            self.lista_pz.append(self.xp[2])
            self.lista_nx.append(self.xn[0])
            self.lista_ny.append(self.xn[1])
            self.lista_nz.append(self.xn[2])
            self.lista_qp.append(self.xp)
            self.lista_qn.append(self.xn)
            self.T=self.T+self.dt
        #print(self.lista_qp)
        #print(self.lista_px)
        #print(self.lista_py)
        #print(self.lista_pz)
            
    def plot(self):
        
        self.fig=plt.figure()
        self.ax=plt.axes(projection='3d')

        self.xlinen=self.lista_nx
        self.ylinen=self.lista_ny
        self.zlinen=self.lista_nz
        self.ax.plot3D(self.xlinen,self.ylinen,self.zlinen,'b')

        self.xlinep=self.lista_px
        self.ylinep=self.lista_py
        self.zlinep=self.lista_pz
        self.ax.plot3D(self.xlinep,self.ylinep,self.zlinep,'r')


        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

        plt.show()



    def Runge_Kutta(self):
        self.Tr=0
        self.lista_vn_kutta=[]
        self.lista_xn_kutta=[(0,0,0)]
        self.lista_vn_kutta.append(self.vi)
        self.lista_nx_kutta=[0]
        self.lista_ny_kutta=[0]
        self.lista_nz_kutta=[0]


        while self.Tr<self.t:
            self.a_kutta=(self.qn*(self.E+np.cross(self.lista_vn_kutta[-1],self.B)))/self.m
            self.k1vx=((self.qn*(self.E+np.cross(self.lista_vn_kutta[-1],self.B)))/self.m)*self.dt
            self.k1x=self.lista_vn_kutta[-1]*self.dt
            self.k2vx=((self.qn*(self.E+np.cross(self.lista_vn_kutta[-1],self.B))/self.m)+self.k1vx*0.5)*self.dt
            self.k2x=(self.lista_vn_kutta[-1]+((self.k1vx)/2))*self.dt
            self.k3vx=((self.qn*(self.E+np.cross(self.lista_vn_kutta[-1],self.B))/self.m)+self.k2vx*0.5)*self.dt
            self.k3x=(self.lista_vn_kutta[-1]+((self.k2vx)/2))*self.dt
            self.k4vx=(self.qn*((self.E+np.cross(self.lista_vp[-1],self.B))/self.m)+self.k3vx)*self.dt
            self.k4x=(self.lista_vn_kutta[-1]+self.k3vx)*self.dt
            self.vn_kutta=self.lista_vn_kutta[-1]+(1./6.)*(self.k1vx+2*self.k2vx+2*self.k3vx+self.k4vx)
            self.xn_kutta=self.lista_xn_kutta[-1]+(1./6.)*(self.k1x+2*self.k2x+2*self.k3x+self.k4x)
            self.lista_vn_kutta.append(self.vn_kutta)
            self.lista_xn_kutta.append(self.xn_kutta)
            self.lista_nx_kutta.append(self.xn_kutta[0])
            self.lista_ny_kutta.append(self.xn_kutta[1])
            self.lista_nz_kutta.append(self.xn_kutta[2])
            self.Tr=self.Tr+self.dt
        


    def plot_kutta(self):
        self.fig=plt.figure()
        self.ax=plt.axes(projection='3d')

        self.xline_kutta=self.lista_nx_kutta
        self.yline_kutta=self.lista_ny_kutta
        self.zline_kutta=self.lista_nz_kutta
        self.ax.plot3D(self.xline_kutta,self.yline_kutta,self.zline_kutta,'r')

        self.xlinen=self.lista_nx
        self.ylinen=self.lista_ny
        self.zlinen=self.lista_nz
        self.ax.plot3D(self.xlinen,self.ylinen,self.zlinen,'b')


        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

        plt.show()









c1=Cestica(1,1,0.1,0.1,0.1,0,0,1,0,0,0,0,0,0,0.01,0,20)
#pdb.set_trace()
c1.putanja()
#c1.plot()
c1.Runge_Kutta()
c1.plot_kutta()