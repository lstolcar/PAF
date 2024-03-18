class Particle_P:
    def __init__(self,mass,x_0,v_0):
        self.mass = mass
        self.x_0 = x_0
        self.v_0 = v_0

    def printinfo(self):
        print('Masa cestice = ',self.mass)
        print('Polozaj cestice = ',self.x_0)
        print('Brzina =',self.v_0)
    def ishodiste(self):
        self.x_0 = 0
    def povecanje_brzine(self,dv):
        self.v_0= self.v_0 + dv
        


p1 = Particle_P(10,10,20)
p1.printinfo()
p1.povecanje_brzine(5)
p1.ishodiste()
p1.printinfo()
        