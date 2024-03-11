import matplotlib.pyplot as plt
import numpy as np
def regresija(M,phi):
    M_= sum(M)/len(M)
    phi_= sum(phi)/len(phi)
    #print(M_)
    #print(phi_)
    D=(M_*phi_)/(phi_**2)
    print(D)
    X=[]
    Y=[]
    for x in np.linspace(0,1.2,1000):
        y=D*x
        Y.append(y)
        X.append(x)

    p = np.poly1d( np.polyfit(X, Y, 1) )
    t=np.linspace(0,1.2,1000)




    plt.subplot(2,1,1)
    plt.plot(phi,M,'bo')
    plt.title('Graf linearne regresije')
    plt.xlabel('$ \phi $ [rad]')
    #nisam siguran zasto mi ne prihvaca \varphi
    plt.ylabel('M [Nm]')
    plt.tight_layout()
    plt.plot(X,Y,'r')
    
    plt.subplot(2,1,2)
    plt.title('Graf linearne regresije koristeci polyfit')
    plt.xlabel('$ \phi $ [rad]')
    plt.ylabel('M [Nm]')
    plt.plot(phi,M,'bo')
    plt.plot(t,p(t),'g')
    plt.tight_layout()
    plt.show()






regresija([0.052, 0.124, 0.168, 0.236, 0.284, 0.336],[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] )