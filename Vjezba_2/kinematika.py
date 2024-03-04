import numpy as np
import math as mat
import matplotlib.pyplot as plt

def jednoliko_gibanje():
    F=float(input('Unesite iznos sile: '))
    m=float(input('Unesite iznos mase: '))
    a=[]
    v=[]
    x=[]
    lista=list(range(0,11))
    for t in range(0,11):
        akc=F/m
        brz=akc*t
        put=(akc*t**2)/2
        a.append(akc)
        v.append(brz)
        x.append(put)
    figure, (a1,a2,a3) = plt.subplots(3,1) 
    
        
    a1.plot(lista,a,'r')
    a1.set_title('a-t graf')
    a2.plot(lista,v,'g')
    a2.set_title('v-t graf')
    a3.plot(lista,x)
    a3.set_title('x-t graf')
    
    plt.show()
def jednoliko_gibanje_numericki(F,m):
    a=[]
    v=[]
    x=[]
    t=[]
    for vrijeme in range(0,11):
        akc=F/m
        brz=akc*vrijeme
        put=(akc*vrijeme**2)/2
        a.append(akc)
        v.append(brz)
        x.append(put)
        t.append(vrijeme)
    figure, (a1,a2,a3) = plt.subplots(3,1) 
    
        
    a1.plot(t,a,'r')
    a1.set_title('a-t graf')
    a2.plot(t,v,'g')
    a2.set_title('v-t graf')
    a3.plot(t,x)
    a3.set_title('x-t graf')

    plt.show()

def hitac():
    v0=float(input('Unesite pocetnu brzinu(m/s): '))
    kut=float(input('Unesite kut otklona: '))
    rad=kut*(np.pi/180)
    vx=v0*np.cos(rad)
    vy=v0*np.sin(rad)
    g=9.81
    iksevi=[]
    ipsiloni=[]
    t_nula=[]
    
    for t in np.linspace(0,11,10000):
        x=vx*t
        y=vy*t-(g*t**2)/2
        iksevi.append(x)
        ipsiloni.append(y)
        if 0.1>vy*t-(g*t**2)/2>=0:
            t_nula.append(t)
    
    if t_nula==[]:
        nul_tocka=False
    else:
        nul_tocka=True
    
    plt.subplot(3,1,1)
    plt.plot(iksevi,ipsiloni)
    plt.title('x-y graf')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(3,1,2)
    plt.plot(np.linspace(0,11,10000),iksevi,'r')
    plt.title('x-t graf')
    plt.xlabel('t')
    plt.ylabel('x')

    plt.subplot(3,1,3)
    plt.plot(np.linspace(0,11,10000),ipsiloni,'g')
    if nul_tocka==True:
        plt.plot(t_nula[-1],0,'r',marker='.',markersize=15)
    plt.title('y-t graf')
    plt.xlabel('t')
    plt.ylabel('y')    
    
    plt.show()
    print(t_nula[0])



def hitac_numericki(v0, kut, t, dt=0.01, x0=0, y0=0):
    rad=kut*(np.pi/180)
    ax=0
    ay=-9.81
    vx0=v0*np.cos(rad)
    vy0=v0*np.sin(rad)
    Vx=[]
    Vy=[]
    X=[]
    Y=[]
    Vx.append(vx0)
    Vy.append(vy0)
    X.append(x0)
    Y.append(y0)
    for t in np.arange(0,t+1,dt):
        vx=Vx[-1]+ax*dt
        vy=Vy[-1]+ay*dt
        x=X[-1]+vx*dt
        y=Y[-1]+vy*dt
        Vx.append(vx)
        Vy.append(vy)
        X.append(x)
        Y.append(y)
    print(X)
    plt.subplot(3,1,1)
    plt.plot(X,Y)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(3,1,2)
    plt.plot(np.linspace(0,t+1,len(X)),X,'r')
    plt.title('x-t graf')
    plt.xlabel('t')
    plt.ylabel('x')

    plt.subplot(3,1,3)
    plt.plot(np.linspace(0,t+1,len(Y)),Y,'g')
    plt.title('y-t graf')
    plt.xlabel('t')
    plt.ylabel('y')   
    
    plt.show()


    



jednoliko_gibanje()
jednoliko_gibanje_numericki(50,5)
hitac()
hitac_numericki(50,45,10)


