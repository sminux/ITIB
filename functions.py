'''
Created on 2 апр. 2017 г.

@author: Сергей
'''
from itertools import combinations

quantity = 4
learningKoef = 0.3
X = [0]*16
for i in range(16):
    X[i] = [0]*4  
F = []
F = (0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1)
X = ((1,0,0,0,0),
    (1,0,0,0,1),
    (1,0,0,1,0),
    (1,0,0,1,1),
    (1,0,1,0,0),
    (1,0,1,0,1),
    (1,0,1,1,0),
    (1,0,1,1,1),
    (1,1,0,0,0),
    (1,1,0,0,1),
    (1,1,0,1,0),
    (1,1,0,1,1),
    (1,1,1,0,0),
    (1,1,1,0,1),
    (1,1,1,1,0),
    (1,1,1,1,1))
            
def ParseFunction(input_data):
    X = []
    i = 0
    for i in range(quantity + 1):
        X.append(input_data % 2)
        input_data = (input_data - X[i]) / 2 

def net(w, X):
    net = 0
    i = 0
    for i in range(quantity + 1):
        net += X[i] * w[i]
        i += 1
    return net

def f(net, AF):
    if AF == 0:
        return 1 if net > 0 else 0
    else:
        return 1 if 0.5 * ((net / (1.0 + abs(net))) + 1) >= 0.5 else 0
    
def F_result(X):
    x =[]
    i = 0
    for i in range(quantity + 1):
        if X[i] == 1:
            x[i] = 1
        else:
            x[i] = 0
    if ((x[4] & x[3]) | x[2] | x[1]) == 1:   
        return 1
    else:
        return 0
    

def learning(AF):
    w = [0,0,0,0,0]  
    '''for i in range(16):
        X[i] = (ParseFunction(i))
        F.append(F_result(X[i])) 
    '''
    Y = list(f(net(w, X[i]), 0) for i in range(16))  
    E = sum((F[i]^Y[i] for i in range(16)))
    print('F:  ', F)
    print('Epos# 0 | Y=%s, W=[%.2f, %.2f, %.2f, %.2f, %.2f], E=%d' % (str(Y),w[0],w[1],w[2],w[3],w[4],E)) 
    count = 0
    while E > 0:
        count +=1
        delta = tuple((F[i]-Y[i] for i in range(16)))
        if AF == 0:
            for i in range(quantity + 1):
                w[i] += sum(learningKoef * delta[j] * X[j][i] for j in range(16))
            Y = list(f(net(w, X[i]), 0) for i in range(16))
        else:
            for i in range(quantity + 1):
                w[i] += sum(learningKoef * delta[j] * X[j][i] * ((abs(net(w, X[i])) + net(w, X[i]) + 1) / (2 * (abs(net(w, X[i])) + 1) * (abs(net(w, X[i])) + 1))) for j in range(16))
            Y = list(f(net(w, X[i]), 0) for i in range(16))
        E = sum((F[i]^Y[i] for i in range(16)))
        print('Epos# %d | Y=%s, W=[%.2f, %.2f, %.2f, %.2f, %.2f], E=%d' % (count,str(Y),w[0],w[1],w[2],w[3],w[4],E))

def index(num): #номер набора
    return num[4]+2*num[3]+4*num[2]+8*num[1]

def partly_learning(F, X, sets, flag):
    w = [0,0,0,0,0]
    Y = list(f(net(w,X[i]), 2) for i in range(16))
    E = sum((F[i]^Y[i] for i in range(16)))
    if flag:
        print('Epos# 0 | Y=%s, W=[%.3f, %.3f, %.3f, %.3f, %.3f], E=%d' % (str(Y),w[0],w[1],w[2],w[3],w[4],E))
    count = 1 
    while E>0:
        delta = tuple((F[i]-Y[i] for i in range(16)))
        for i in range(quantity + 1):
            w[i] += sum(learningKoef * delta[index(sets[j])] * sets[j][i] * ((abs(net(w, sets[j])) + net(w, sets[j]) + 1) / (2 * (abs(net(w, sets[j])) + 1) * (abs(net(w, sets[j])) + 1))) for j in range(sets.__len__()))
        Y = list(f(net(w,X[i]), 2) for i in range(16))
        E = sum((F[i]^Y[i] for i in range(16)))
        if flag:
            print('Epos# %d | Y=%s, W=[%.3f, %.3f, %.3f, %.3f, %.3f], E=%d' % (count,str(Y),w[0],w[1],w[2],w[3],w[4],E))
        count +=1
        if count > 64: return -1 #выход из функции при условии (если наборы не найдены)
    return count - 1

def learning_sets():
    for i in range(2,16):
        combinations_full = list(combinations(X, i)) 
        print('Mount of ', i,' vectors')
        for sets in combinations_full:
            flag = 1
        count = partly_learning(F, X, sets, 0)
        if count > 0:
            print(sets)
            partly_learning(F, X, sets, 1)
            flag = 0
            break
        if flag == 0: break
   