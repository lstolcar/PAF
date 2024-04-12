import calculus as calc
import matplotlib.pyplot as plt

def func(x):
    return (5*x**3)-(2*x**2)+(2*x)-3
def analiticko(x):
    return (15*x**2)-(4*x)+2 
def funkcija(x):
    return (2*x**2)+3

calc.metoda_prva(func,1,0.01)#'two-step')
calc.analiticko(x=0.01)
calc.metoda_druga(func,analiticko,-2,2,0.01,0.1,'two-step')
calc.graf_deriviranje()
calc.metoda_prva_integriranje(funkcija,1,0,1000)
calc.metoda_druga_integriranje(funkcija,1,0,1000)
calc.graf_integriranje(1000)
