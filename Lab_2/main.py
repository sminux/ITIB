'''
Created on 3 апр. 2017 г.

@author: Сергей
'''
import math 
import functions

print('ITIB Laboratory work #2. Application of a single-layer neural network with a linear activation function for the prediction of time series')

p = 4 #количество нейронов
Epos = 4000
X = [0]*(p+1)
a = -2
b = 2
n = 0.5
'''
авторегрессионная модель, когда прогнозируемое значение ряда в момент времени n>m выражается 
через известные значения в предыдущие моменты времени
'''    
n = (b - a) * p + 1
F_true = [0]*n
i = 0
for i in range(n):
    F_true[i] = math.sin(a + 0.25 + 1)
    i += 1

epsi = 0.0
#d = 0.0
epo = 0
for epo in range(Epos):
    epsi = 0.0
    i = 0
    j = 1
    for i in range(n - p):
        for j in range(p + 1):
            X[0] = 1
            X[j] = F_true[i + j - 1]
            #print("x{%d}={%f} " %(j, F_true[i + j - 1]))
        w = [0]*(p+1) 
        d = functions.prediction(X, F_true[i + p], w)/(n - p)
        epsi += d
        
print("Epsilon = ", math.sqrt(epsi))

functions.printWeights(w)

x = b
i = n - p 
j = 1
for i in range(n + n - p - 1):
    for j in range(p + 1):
        X[0] = 1
        X[j] = F_true[i + j - 1]
    y = functions.net(X, w)
    x += 0.25
    mistake = (math.sin(0.3 * x) + 1) - y
    F_true.append(y)
    print(y)
    #print("x = %d   y = %.3f   mistake = %d" %(x, y, mistake))
    

    