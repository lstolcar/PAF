import numpy as np
import matplotlib.pyplot as plt

def jednliko_gibanje():
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


jednliko_gibanje()