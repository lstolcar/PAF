import calculus as calc
import matplotlib.pyplot as plt
def funkcija(x):
    return (2*x**2)+3

calc.metoda_prva_integriranje(funkcija,1,0,1000)
calc.metoda_druga_integriranje(funkcija,1,0,1000)
calc.graf(1000)
