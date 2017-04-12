'''
Created on 4 апр. 2017 г.

@author: Сергей
'''
import math

p = 9
X = []*(p+1)
a = -2
b = 2
n = 0.5 
        
def prediction(X, t, w):    
    net = 0
    delta = 0.0
    net += sum(X[i]*w[i] for i in range(p+1))
    delta = t - net
    i = 0
    for i in range(p+1):
        w[i] += (delta * n * X[i])
    return delta ** 2

def net(X, w):
    net = 0
    net += sum(X[i]*w[i] for i in range(p+1))
    return net


X = [0]*(p + 1)

def learning(num_of_epos):   
    n = (b - a) * 4 + 1 
    F = [0]*n
    i = 0
    for i in range(n):
        F[i] = math.sin((a + i - 1))#0.4 * math.sin(0.3 * (a + (0.25 * i))) - 0.5 
    print()
    print("Number of epos: ", num_of_epos)
    epo = 0
    for epo in range(num_of_epos):
        e = 0.0
        i = 0
        j = 1
        for i in range(n - p):
            for j in range(p + 1):
                X[0] = 1
                X[j] = F[i + j - 1]
            w = [0]*(p+1) 
            d = prediction(X, F[i + p], w)/(n - p)
            e += d
        
    print("ε = ", math.sqrt(e))

    for i in range(p):
        print('w[%s] = %.3f' %(i, w[i]), end=' ')
        
    x = b
    i = n - p 
    j = 1
    print("\nx:       y:       σ:")
    for i in range(n + n - p - 1):
        for j in range(p + 1):
            X[0] = 1
            X[j] = F[i + j - 1]
        y = net(X, w)
        #x += 0.25
        mistake = (math.sin(x) - 1) - y#0.4 * math.sin(0.3 * (0.25 * x)) - 0.5 
        F.append(y)
        print("%.3f   %.3f   %.3f" %(x, y, mistake))