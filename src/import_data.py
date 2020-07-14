# Author: Ulises Olivares
# June 8, 2020
# uolivares@unam.mx
import csv
import glob

class ImportCSV:
    def __init__(self, file):
        self.file = file
        print("File path: " + self.file)

    def explorePath(self, path):
        return glob.glob(path+"*.csv")

    def importCSV(self, files):
       # this works only for one file
       #print ("FileName: " +str(self.file))
       X = [0] * len(files)
       Y = [0] * len(files)
       for i in range  (0,len(files)):
           X[i] = []
           Y[i] = []
           with open(files[i], encoding='utf-8-sig') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    #print("Row: " + str(len(row) /2))
                    for j in range(0, len(row)):
                        if j % 2 == 0 and row[j] != '':
                            #print(row[i])
                            X[i].append(float(row[j]))
                        elif row[j] and row[j]!= '':
                            #print(row[i])
                            Y[i].append(float(row[j]))
       #print(X)
       #print(Y)

       return X, Y
