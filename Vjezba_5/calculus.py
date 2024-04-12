import numpy as np
import math as mt
import matplotlib.pyplot as plt
from fractions import Fraction

def metoda_prva (func,T,eps=0.01,metoda='three-step'):
    x=T
    if metoda=='two-step':
        d=(func(T+eps)-func(T))/eps
        print(round(d,4))
    else:
        d=(func(T+eps)-func(T-eps))/(2*eps)
        print(round(d,4))

def metoda_druga(func,analiticko,x_i,x_f,eps,epsilon,metoda='three-step'):
    N=int(abs(x_f-x_i)/eps)
    n=int(abs(x_f-x_i)/epsilon)
    lista_tocaka_1=[]
    lista_tocaka_2=[]
    lista_tocaka_a=[]
    lista_derivacija_1=[]
    lista_derivacija_2=[]
    lista_derivacija_a=[]
    for x in np.linspace(x_i,x_f,N):
        a=x
        #der = analiticko(x)
        #lista_derivacija_a.append(der)
        if metoda=='two-step':
            d=(func(a+eps)-func(a))/(eps)
            lista_tocaka_1.append(a)
            lista_derivacija_1.append(d)
        else:
            d=(func(a+eps)-func(a-eps))/(2*eps)
            lista_tocaka_1.append(a)
            lista_derivacija_1.append(d)
    for x in np.linspace(x_i,x_f,n):
        a=x
        #der = analiticko(x)
        #lista_derivacija_a.append(der)
        if metoda=='two-step':
            d=(func(a+epsilon)-func(a))/(epsilon)
            lista_tocaka_2.append(a)
            lista_derivacija_2.append(d)
        else:
            d=(func(a+epsilon)-func(a-epsilon))/(2*epsilon)
            lista_tocaka_2.append(a)
            lista_derivacija_2.append(d)
    for x in np.linspace(x_i,x_f,10000):
        a=x
        der = analiticko(x)
        lista_derivacija_a.append(der)
        lista_tocaka_a.append(x)


            
    #print(lista_derivacija_a)
    #print(lista_tocaka)

    #plt.plot(lista_tocaka_1,lista_derivacija_1,'o',markersize=1)
    plt.plot(lista_tocaka_2,lista_derivacija_2,'o',markersize=1)
    #plt.plot(lista_tocaka_a,lista_derivacija_a,'r',markersize=2)
    plt.show()

        
    



def analiticko(x):
    d=(15*x**2)-(4*x)+2
    return d
    #print(round(d,4))



        
    

def func(x):
    return (5*x**3)-(2*x**2)+(2*x)-3
 
def metoda_prva_integriranje(funkcija,gornja,donja,N):
    dx=(abs(float(gornja)-float(donja)))/(N)
    sumaG = 0
    sumaD = 0
    sumag=0
    sumad=0
    lista_G=[]
    lista_D=[]
    for i in range(0,N):
        sumaG += funkcija((i+1)*dx)*dx
        sumaD += funkcija(i*dx)*dx
    print(sumaG,sumaD)
    lista_N=[]
    for n in np.arange(50,N,50):
        lista_N.append(n)
        delta_x=(abs(float(gornja)-float(donja)))/(n)
        for i in range(0,n):
            sumag += funkcija((i+1)*delta_x)*delta_x
            sumad += funkcija(i*delta_x)*delta_x
        lista_D.append(sumad)
        lista_G.append(sumag)
        sumag=0
        sumad=0
    #print(lista_G)
    #print(lista_D)
    #print(lista_N)
    plt.plot(lista_N,lista_G,'o')
    plt.plot(lista_N,lista_D,'o')
            

    #print(dx)
        
    #print(gornja)
    #print(donja)

def metoda_druga_integriranje(funkcija,gornja,donja,N):
    dx=(abs(float(gornja)-float(donja)))/(N)
    integral=0
    lista_integrala=[]
    lista_N=[]
    for n in np.arange(50,N,50):
        lista_N.append(n)
        delta_x=(abs(float(gornja)-float(donja)))/(n)
        for i in range(0,n):
            integral+=(delta_x/2)*(funkcija(i*delta_x)+funkcija((i+1)*delta_x))
        lista_integrala.append(integral)
        integral=0
    #print(lista_integrala)
    #print(lista_N)

    plt.plot(lista_N,lista_integrala,'o')
    return lista_N,lista_integrala
     

def graf(N):
    lista_N=[]
    lista_integracija=[]
    for n in np.arange(50,N,50):
        lista_N.append(n)
        lista_integracija.append(Fraction(11,3))
    plt.plot(lista_N,lista_integracija)
    plt.show()






def funkcija(x):
    return (2*x**2)+3
def int_analiticki():
    print(125/3)





#metoda_prva(func,1,0.01)#'two-step')
analiticko(x=0.01)
metoda_druga(func,analiticko,-2,2,0.01,0.1)
#metoda_prva_integriranje(funkcija,1,0,1000)
#metoda_druga_integriranje(funkcija,1,0,1000)
#graf(1000)