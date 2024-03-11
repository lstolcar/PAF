import numpy as np
import matplotlib.pyplot as plt

def fun_koor():
    x1=float(input('Unesite x1 kordinatu: '))
    y1=float(input('Unesite y1 kordinatu: '))
    x2=float(input('Unesite x2 kordinatu: '))
    y2=float(input('Unesite y2 kordinatu: '))
    k=(y2-y1)/(x2-x1)
    u=y1-k*x1
    lista_x=[]
    lista_y=[]
    for x in np.linspace(-5,5,10):
        y=k*x+u
        lista_x.append(x)
        lista_y.append(y)
    if u > 0 and k==1:
        print('y=x + {}'.format(u))
    elif u > 0 and k!=1:
        print('y={}x+{}'.format(k,u))
    elif u == 0 and k==1:
        print('y=x')
    elif u==0 and k!=1:
        print('y={}x'.format(k))
    elif u < 0 and k==1:
        print('y=x{}'.format(u))
    else:
        print('y={}x{}'.format(k,u))
    pdf=input('Zelite li graf spremiti kao PDF? ')
    if pdf.lower()=='da' or pdf.lower()=='zelim':
        ime=input('Nazovite svoj PDF: ')
        plt.plot(lista_x,lista_y)
        plt.savefig('{}.pdf'.format(ime))

    else:
        plt.plot(lista_x,lista_y)
        plt.show()






fun_koor()