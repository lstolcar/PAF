import numpy as np
import math as mt
import matplotlib.pyplot as plt

def metoda_prva (func,T,eps=0.01,metoda='three-step'):
    x=T
    if metoda=='two-step':
        d=(func(T+eps)-func(T))/eps
        print(round(d,4))
    else:
        d=(func(T+eps)-func(T-eps))/(2*eps)
        print(round(d,4))

def metoda_druga(func,analiticko,x_i,x_f,eps,N,metoda='three-step'):
    lista_tocaka=[]
    lista_derivacija=[]
    lista_derivacija_a=[]
    for x in np.linspace(x_i,x_f,N):
        a=x
        der = analiticko(x)
        lista_derivacija_a.append(der)
        if metoda=='two-step':
            d=(func(a+eps)-func(a))/(eps)
            lista_tocaka.append(a)
            lista_derivacija.append(d)
        else:
            d=(func(a+eps)-func(a-eps))/(2*eps)
            lista_tocaka.append(a)
            lista_derivacija.append(d)

            
    print(lista_derivacija_a)
    #print(lista_tocaka)

    plt.plot(lista_tocaka,lista_derivacija,'o',markersize=3)
    plt.plot(lista_tocaka,lista_derivacija_a,'r',markersize=2)
    plt.show()

        
    



def analiticko(x):
    d=(3*x**2)+4*x
    return d
    #print(round(d,4))



        
    

def func(x):
    return (x**3)+2*x**2
 
def metoda_prva_integriranje(funkcija,gornja,donja,N):
    dx=abs(gornja-donja)/N
    sumaG=0
    sumaD=0
    for i in range(0,N):
        sumaG += funkcija((i+1)*dx)*dx
        sumaD += funkcija(i*dx)*dx
    print(sumaG,sumaD)

def metoda_druga_integriranje(funkcija,gornja,donja,N):
    dx=abs(gornja-donja)/N
    integral=0
    for i in range(0,N):
        integral+=(dx/2)*(funkcija(i*dx)+funkcija((i+1)*dx))
    print(integral)  









def funkcija(x):
    return x**2
def int_analiticki():
    print(125/3)





#metoda_prva(func,1,0.01)#'two-step')
#analiticko(x=0.01)
#metoda_druga(func,analiticko,-10,10,0.01,150)
metoda_prva_integriranje(funkcija,0,5,1000)
metoda_druga_integriranje(funkcija,0,5,1000)