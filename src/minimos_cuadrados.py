from sympy import *
import numpy as np
import statistics as st

x = Symbol('x')

class MinimosCuadrados:
    def __init__(self):
        self.x = 1  #esto no es nada. solo lo puse para rellenar el espacio

    def RegresionLineal(self, X, Y):
        sumXY = 0
        sumX = 0
        sumY = 0
        sumX2 = 0

        for i in range (0, len(X)):
            sumXY = sumXY + X[i]*Y[i]
            sumX = sumX + X[i]
            sumY = sumY + Y[i]
            sumX2 = sumX2 + X[i]**2
        a1 = round((len(X) * sumXY - (sumX * sumY))/ ((len(X) * sumX2) - sumX**2), 4)
        a0 = round(st.mean(Y) - a1 * st.mean(X),4)

        f = a0 + a1 * np.array(X)
        F = a0 + a1 * x
        print("Regresion Lineal: y = "+ str(a0) + " + " + str(a1) + " x")
        self.Error(X, Y, F)
        return F

    def Error(self, X, Y, f):
        error = 0
        for i in range (0, len(X)):
            error = error + (Y[i] - f.subs(x, X[i]))**2
        print ("Error: "+str(error))
        return error

    def RegresionPoli(self,X,Y,orden):
        coefX = [0] * (orden * 2)
        XiY = [0] * (orden + 1)
        n = len(X)
        for i in range (0, n):
            for j in range (0, len(coefX)):
                coefX[j] = coefX[j] + X[i]**(j+1)
                if(j< orden+1):
                    XiY[j] = XiY[j] + (X[i]**j * Y[i])
        #print(coefX)
        #print(XiY)
        SistemaEc = np.ndarray(shape=(orden + 1, orden + 1), dtype= 'float')
        for i in range(0, orden + 1):
            for j in range(i, orden + 1):
                SistemaEc[i][j]=coefX[i+j-1]
                SistemaEc[j][i]=SistemaEc[i][j]
        SistemaEc[0][0] = n
        A = np.linalg.solve(SistemaEc,XiY)

        f = A[0]                        #arreglo con valores discretos
        F = A[0]                        #funcion completa
        for i in range (1, orden + 1):
            f = f + A[i] * (np.array(X)**i)
            F = F + A[i] * x ** i

        print("Regresion Polinomial: "+str(A[0]), end="")
        for i in range (1, orden+1):
            print(" + "+ str(A[i])+" x^"+str(i), end=" ")
        print("")
        self.Error(X, Y, F)
        return F

    def Coeficientes(self,X,Y,orden):
        coefX = [0] * (orden * 2)
        XiY = [0] * (orden + 1)
        n = len(X)
        for i in range (0, n):
            for j in range (0, len(coefX)):
                coefX[j] = coefX[j] + X[i]**(j+1)
                if(j< orden+1):
                    XiY[j] = XiY[j] + (X[i]**j * Y[i])
        #print(coefX)
        #print(XiY)
        SistemaEc = np.ndarray(shape=(orden + 1, orden + 1), dtype= 'float')
        for i in range (0, orden + 1):
            for j in range (i, orden + 1):
                SistemaEc[i][j]=coefX[i+j-1]
                SistemaEc[j][i]=SistemaEc[i][j]
        SistemaEc[0][0] = n
        A = np.linalg.solve(SistemaEc,XiY)
        return A

