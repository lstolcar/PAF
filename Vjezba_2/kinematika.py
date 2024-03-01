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
        if 0.1>vy*t-(g*t**2)/2>=0 and t>=1:
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
        plt.plot(t_nula[0],0,'r',marker='.',markersize=15)
    plt.title('y-t graf')
    plt.xlabel('t')
    plt.ylabel('y')    
    
    plt.show()
    print(t_nula[0])

jednoliko_gibanje()
hitac()

