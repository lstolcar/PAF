import numpy as np


def arithm(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10):
    a=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
    x_=float(sum(a))/10
    print(x_)
    brojnik=[]
    for i in range(len(a)):
        b=float((a[i]-x_)**2)
        brojnik.append(b)
        b=0
    sigma=np.sqrt(float(sum(brojnik)/(len(a)*(len(a)-1))))
    print(sigma)
    


arithm(1,2,3,4,5,6,7,8,9,10)