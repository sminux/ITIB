'''
Created on 3 апр. 2017 г.
@author: sminux
'''
import math
import matplotlib.pyplot

print('ITIB Laboratory work #2. Application of a single-layer neural network with a linear activation function for the prediction of time series')

W = [0]*15
X = [0]*40
y = [0]*20
d = [0]*20
p = 11
n = 0.1
a = -5.0
b = 3.0
f = 0.0
eps = 0.0
net = 0.0
step = (b - a) / 20
for p in range(15): 
    k = 0
    era = 25
    j = 0

    for j in range(20):
        X[j] = math.sin(a + j*step - 1)
    j = 0
    i = 0
    for j in range(era):
        for i in range(20-p):
            net = 0.0
            o = 0
            for o in range(p):
                net += W[o] * X[i + o]
            d[i] = X[i + p] - net   
            u = 0
            if d[i] != 0:
                for u in range(p):
                    W[u] = W[u] + X[i + u] * d[i] * n

    i = 0
    for i in range(20):
        print('X: %.6f' %(X[i]))
    print('W:')
    for i in range(p):
        print('[%.3f' %(W[i]), end=']')
    
    i = 20 - p
    for i in range(40 - p):
        net = 0.0
        o = 0
        for o in range(p):
            net = net + W[o] * X[i + o]
        X[i + p] = net
        y[i + p - 20] = math.sin(b + (i + p - 20)*step - 1)
        f = y[i + p - 20] - X[i + p]
        eps = eps + f**2

    i = 20
    for i in range(40):
        #print('X[', i, ']: ', X[i],'| Y:', y[i - 20] )
        #print('ε =', math.sqrt(eps))
        print(y[i - 20])
    
    f = 0.0
    eps = 0.0
    net = 0.0
    m = 0
    for m in range(p):
        W[m] = 0

x =[]
'''
y_norm = []
for i in range(20):
    x.append(a + i*step)
    y_norm.append(math.sin(a + i*step - 1))
matplotlib.pyplot.plot(x, y_norm) 
matplotlib.pyplot.xlabel(r'$x$') 
matplotlib.pyplot.ylabel(r'$f(x) non-prediction$') 
matplotlib.pyplot.grid(True) 
matplotlib.pyplot.show() 
'''
for i in range(20):
    x.append(a + i*step)
matplotlib.pyplot.plot(x, y) 
matplotlib.pyplot.xlabel(r'$x$') 
matplotlib.pyplot.ylabel(r'$f(x) prediction$') 
matplotlib.pyplot.grid(True) 
matplotlib.pyplot.show() 
