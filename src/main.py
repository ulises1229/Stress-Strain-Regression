from minimos_cuadrados import MinimosCuadrados
from chebyshev import PolinomiosChebyshev
from spline import Spline
from graph import Graph
from import_data import ImportCSV
import time
from sympy import abc

import os

from sympy import *

path = os.getcwd() + "/CSV/"

# Object declaration
objImp = ImportCSV(path)
objG = Graph()

files = objImp.explorePath(path)
print(files)
X, Y = objImp.importCSV(files)

#print("X size: " + str(len(X)))
#print("Y size: " + str(len(Y)))


x = Symbol('x')

#orden = 10
"""X = [0] * 59
for i in range(0, 59):
    X[i] = 60+i
Y = [667,660,665,682,698,715,735,754,774,796,818,841,862,881,900,916,930,943,956,969,981,994,1008,1023,1036,1051,1067,1084,1101,1118,1135,1150,1165,1178,1191,1204,1217,1230,1242,1253,1263,1272,1280,1288,1296,1303,1311,1318,1324,1331,1337,1344,1350,1357,1364,1371,1378,1386,1392]
"""
#n = len(X)

#  M I N I M  O S  C U A D R A D O S  #
"""objMC = MinimosCuadrados()

print("* * * * * * * * * * * * * * * * * * * *")

# l i n e a l
F1 = objMC.RegresionLineal(X, Y)
# objMC.Error(X,Y,F1)

print("* * * * * * * * * * * * * * * * * * * *")

# p o l i n o m i a l
F2 = objMC.RegresionPoli(X,Y,orden)
# objMC.Error(X,Y,F2)


print("* * * * * * * * * * * * * * * * * * * *")"""

#  P O L I N O M I O S  D E  C H E B Y S H E V  #
"""f = F2
objPC = PolinomiosChebyshev(min(X), max(X), F2)
# objPC.Polinomios(x, 4)
F3 = objPC.Regresion(orden)
objPC.Error(F3, X)"""


print("* * * * * * * * * * * * * * * * * * * *")

#  S P L I N E  #
orden = 8             # grado
nudos = 15              # numero de nudos



for i in range(0, len(files)):
    start = time.time()
    print("------------------------------------------")
    print("Runing Sample M" +str(i+1) + "...")
    objS = Spline()
    F4 = objS.RegresionSpline(X[i], Y[i], orden, nudos)
    #print("Function " + str(i) + ": " + str(F4))
    objS.Error(X[i], Y[i], F4)
    print("Generation graph...")
    #  graph function
    objG.addScatter(X[i], Y[i], "green")
    objG.addLineFunction(F4, min(X[i]), max(X[i]))
    objG.displayPlot(("Regresión Spline " + str(i+1)) , "x", "y")
    print("Sample M" + str(i + 1) + " Generated correctly!")
    print("------------------------------------------")
    end = time.time()
    print("Elapsed time:  " + str((end -start) / 60) + " minutes" )





#  g r a f i c a
"""
objG.addScatter(X, Y, "red")
objG.addLineFunction(F1, min(X), max(X))
objG.addLineFunction(F2, min(X), max(X))
objG.displayPlot("Minimos cuadrados", "x", "y")

objG.addScatter(X, Y, "blue")
objG.addLineFunction(F2, min(X), max(X))
objG.addLineFunction(F3, min(X), max(X))
objG.displayPlot("Polinomios de Chebyshev", "x", "y")"""
