'''
Created on 4 апр. 2017 г.

@author: Сергей
'''
import math

p = 4 #количество нейронов
X = []*(p+1)
a = -2
b = 2
n = 0.5

def printWeights(w):
    i = 0
    for i in range(p+1):
        print("w[%d] = %f" %(i, w[i]))
        
def prediction(X, t, w):   
    #w = [0]*(p+1) 
    net = 0
    delta = 0
    net += sum(X[i]*w[i] for i in range(p+1))
    delta = t - net
    #print("net = %d  |  delta = %f" %(net, delta))
    i = 0
    for i in range(p+1):
        w[i] += abs(delta * n * X[i])
    #print(delta*delta)
    #printWeights(w)
    return delta*delta

def net(X, w):
    net = 0
    net += sum(X[i]*w[i] for i in range(p+1))
    return net