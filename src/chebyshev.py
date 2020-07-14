from sympy import *
import numpy as np

x = Symbol('x')

class PolinomiosChebyshev:
    def __init__(self, xmin, xmax, f):
        self.xmin = xmin
        self.xmax = xmax
        self.f = f

    def Polinomios(self, x, j):
        T = [0] * (j+1)
        for i in range(0, j+1):
            if i == 0:
                T[i] = 1
            elif i == 1:
                T[i] = x
            else:
                T[i] = 2 * x * T[i-1] - T[i-2]
        #print(T[-1])
        return T[-1]                                                 # último elemento de la lista: polinomio de grado j

    def Regresion(self, orden):
        n = orden
        m = n + 1
        zi = [0] * (m+1)                                                          # xi y zi solo tienen valores de 1 a m
        xi = [0] * (m+1)                                                            # así que se ignora el elemento cero
        zi2 = [0] * (m+1)

        for i in range(1, m+1):
            zi[i] = - np.cos(((2*i-1)*np.pi)/(2*m))
            xi[i] = ((1/(np.cos(np.pi/(2*m)))) * zi[i] + 1)/2 * (self.xmax - self.xmin) + self.xmin
            #zi2[i] = (1/sec(pi/(2*m)) * 2 * xi[i] - self.xmin) *2 / (self.xmax - self.xmin) - 1

        theta = [0] * (n+1)                                                            # para tener valores de 0 hasta n
        for i in range(1, m+1):
            theta[0] = theta[0] + self.f.subs(x, xi[i])
        theta[0] = theta[0] * 1/m

        for j in range(1, n+1):
            for i in range(1, m+1):
                Tj = self.Polinomios(x, j)
                theta[j] = theta[j] + self.f.subs(x, xi[i]) * Tj.subs(x, zi[i])
            theta[j] = theta[j] * 2/m

        F = theta[0] * 1                                                               # caso j = 0, el polinomio T0 = 1
        for j in range(1, n+1):
            Tj = self.Polinomios(x, j)
            F = F + theta[j] * self.Polinomios(x, j).subs(x,(np.cos(np.pi/(2*m))) * ((2*(x-self.xmin))/(self.xmax-self.xmin))-1)

        F = simplify(F)
        print("La funcion obtenida con minimos cuadrados se aproxima usando Polinomios de Chebyshev como: " +str(F))
        return F

    def Error(self, F, X):
        error = 0
        for i in range(0, len(X)):
            error = error + (self.f.subs(x, X[i]) - F.subs(x, X[i])) ** 2
        print("Error: " + str(error))
        return error