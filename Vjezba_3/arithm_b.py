import numpy as np

def arithm_b(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10):
    a=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
    print(np.mean(a))
    print(np.std(a)*(np.sqrt(1./(len(a)-1))))
    
   



arithm_b(1,2,3,4,5,6,7,8,9,10)