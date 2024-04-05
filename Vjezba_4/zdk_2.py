import numpy as np
import matplotlib.pyplot as plt
import particle as prt
#p1 = prt.Particle(10,60,0,0)
#D_a =(((p1.v_0)**2)/(-p1.ay))*np.sin(2*p1.kut)
#p1.range()
#D_n=p1.D_n
#print(D_a)
#print(D_n)
lista_err=[]
lista_dt=[]
p1 = prt.Particle(10,60,0,0)
for t in np.linspace(0.00001,0.1,300):
    #p1 = prt.Particle(10,60,0,0)
    D_a =(((p1.v_0)**2)/(-p1.ay))*np.sin(2*p1.kut)
    p1.range(t)
    Err =( (abs(D_a - p1.D_n))/D_a)*100
    lista_err.append(Err)
    lista_dt.append(t) 
    p1.reset()

plt.plot(lista_dt,lista_err)
plt.ylabel('Absolute relative error [%]')
plt.xlabel('dt [s]')
eq=('$ (Err)= \\frac{|D_{analitical}-D_{numerical}|}{D_{analitical}}\cdot (100\\%) $')
plt.text(0.012,9, eq,{'fontsize': 15})
plt.show()