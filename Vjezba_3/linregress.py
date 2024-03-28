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
    for x in np.linspace(0,1.1,1000):
        y=D*x
        Y.append(y)
        X.append(x)

    p = np.poly1d( np.polyfit(X, Y, 1) )
    t=np.linspace(0,1.1,1000)




    plt.subplot(2,1,1)
    plt.plot(phi,M,'bo')
    plt.title('Graf linearne regresije')
    plt.xlabel('$ \\varphi $ [rad]')
    plt.xticks(np.arange(0,1.2,step=0.2))
    plt.yticks(np.arange(0,0.36,step=0.05))
    plt.ylabel('M [Nm]')
    plt.tight_layout()
    plt.plot(X,Y,'r')
    plt.legend(['data','fit'])
    plt.figtext(0.3,0.85,'y={}x'.format(round(D,2)))
    plt.subplot(2,1,2)
    plt.title('Graf linearne regresije koristeci polyfit')
    plt.xlabel('$ \\varphi $ [rad]')
    plt.yticks(np.arange(0,0.36,step=0.05))
    plt.ylabel('M [Nm]')
    plt.ylabel('M [Nm]')
    plt.plot(phi,M,'bo')
    plt.plot(t,p(t),'g')
    plt.legend(['data','fit'])
    plt.figtext(0.3,0.35,'y={}x'.format(round(D,2)))
    plt.tight_layout()
    plt.show()






regresija([0.052, 0.124, 0.168, 0.236, 0.284, 0.336],[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] )