from sympy import *
import numpy as np
import glob
from minimos_cuadrados import MinimosCuadrados

x = Symbol('x')

class Spline:
    def __init__(self):
        self.x = 1



    def FuncionesBase(self, k , m, nudos):
        m = m - 1
        g = [0] * (k + m + 1)
        for i in range(0, k + 1):
                g[i] = x ** i
        for i in range(k + 1, k + m + 1):
            # j de 1 a m
            g[i] = (x - nudos[i - k]) ** k
        return g

    def MinimosCuadrados(self, X, Y, coefX, XiY, funcionBase):

        for i in range(0, len(funcionBase)):
            for j in range(0, len(funcionBase)):
                for k in range(0, len(X)):
                    coefX[i][j] = coefX[i][j] + funcionBase[i].subs(x, X[k]) * funcionBase[j].subs(x, X[k])
            for k in range (0, len(X)):
                XiY[i] = XiY[i] + funcionBase[i].subs(x, X[k]) * Y[k]

        SistemaEc = np.ndarray(shape=(len(funcionBase), len(funcionBase)), dtype= 'float')

        for i in range(0, len(funcionBase)):
            for j in range(i, len(funcionBase)):
                SistemaEc[i][j]=coefX[i][j]
                SistemaEc[j][i]=SistemaEc[i][j]
        A = np.linalg.solve(SistemaEc,XiY)

        f = 0
        for i in range(0, len(funcionBase)):
            f = f + A[i] * funcionBase[i]
        return f

    def RegresionSpline(self, X, Y, k , m):
        j = k - 1 #orden maximo de la derivada

        ancho = (max(X) - min(X)) / m
        nudos = [0] * (m+1)
        for i in range(0, m + 1):
            nudos[i] = min(X) + i * ancho

        g = self.FuncionesBase(k, m, nudos)
        n = len(g)
        """
        objMC = MinimosCuadrados()
        beta = objMC.Coeficientes(X, Y, m + k + 1)              #devuelve un arreglo de coeficientes de tamaño m + k + 1

        r = 0
        for i in range (1, len(beta)):
            r = r + beta[i]*g[i]
        print(r)
        return r
        """
        coefX = np.zeros(((len(g)), (len(g))))
        XiY = np.zeros(len(g))
        f = self.MinimosCuadrados(X, Y, coefX, XiY, g)

        f = simplify(f)

        print("Regresión Spline: " + str(f))
        return f

    def Error(self, X, Y, f):
        error = 0
        for i in range (0, len(X)):
            error = error + (Y[i] - f.subs(x, X[i]))**2
        print ("Error: "+str(error))
        return error
