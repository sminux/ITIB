'''
Created on 2 мая 2017 г.

@author: Сергей
'''
#import matplotlib
from pylab import *
from PIL import Image
'''
f = open('file.txt', 'w')
f.write('string1\n')
f.write('sting2')
f.close()
# Проверяем, записались ли значения
f = open('file.txt', 'r')
print(f.read())
f.close()


def getArray(file):
    arr = [0]*36
    im = array(Image.open(file)) #проверяем последний цвет каждого элемента массива
    for i in range(6):
        for j in range(6):
            let = im[i][j]
            if let[-1] == 0:
                arr[i*6 + j] = -1
            else:
                arr[i*6 + j] = 1
    return arr
                
ideal = [[]]*3
ideal[0] = getArray('circle.png') 
ideal[1] = getArray('arc.png') 
ideal[2] = getArray('loop.png') 


x = [100,100,400,400] 
y = [200,300,200,300] 
plot(x,y,'r*') 
plot(x[:2],y[:2])  

axis('off')
imshow(im)
show()
'''




'''
width = 3
length = 5
dim = width * length

i_2 = [[1,   1,  1],    #2
     [-1, -1,  1],      #
     [1,   1,  1],      #
     [1,  -1, -1],      #
     [1,   1,  1]]      #
                        #
i_4 = [[ 1, -1, 1],     #4
     [ 1, -1, 1],       #
     [ 1,  1, 1],       #
     [-1, -1, 1],       #   Эталоны
     [-1, -1, 1]]       #
                        #
i_8 = [[1,  1,  1],     #8
     [ 1, -1,  1],      #
     [ 1,  1,  1],      #
     [ 1, -1,  1],      #
     [ 1,  1,  1]]      #

'''
#правило Хебба (обучение за один такт)
'''

def toArray(arr):
    new_array = [0]*dim
    for i in range(length):
        for j in range(width):
            new_array[i*width + j] = arr[i][j]
    return new_array

def getWeight(arr):
    W = [0] * dim       #INIT
    for i in range(dim):
        W[i] = [0] * dim
                
    for i in range(dim):
        for j in range(dim):
            if i == j:
                W[i][j] = 0 #обнуляем главную диагональ
            else:
                W[i][j] += arr[i] * arr[j]
    return W

def NET(prew_arr, W, arr, new_arr, count):
    count += 1
    if count > 10:
        return False
     
    out = [0]*dim
    for i in range(dim):
        net = 0
        for j in range(dim):
            net += arr[j] * W[j][i]
        if net > 0:
            out[i] = 1
        elif net < 0:
            out[i] = -1
            
    for i in range(dim):
        if out[i] != prew_arr[i]:
            NET(arr, W, prew_arr)



w = [0] * dim
for i in range(dim):
        w[i] = [0] * dim
        
idol = []
for i in range(3):
    idol.append([])
    
idol[0] = toArray(i_2)
idol[1] = toArray(i_4)
idol[2] = toArray(i_8)

w = []
for i in range(3):
    w.append([])
    
for i in range(3):
    w[i] = getWeight(idol[i])

#for i in range(dim):
#        for j in range(dim):
#            print(w[i][j], end = ' ')
#        print()
        
#print(NET(toArray(i_2), w, toArray(i_2)))

check1 = NET(idol[i], w, idol[i], [], 0)
check2 = NET(idol[i], w, idol[i], [], 0)
check3 = NET(idol[i], w, idol[i], [], 0)
    
print("Распознать первый эталон не удалось") if check1 == False else "Первый эталон"
print("Распознать второй эталон не удалось") if check2 == False else "Второй эталон"
print("Распознать третий эталон не удалось") if check3 == False else "Третий эталон"

'''

width = 6
length = 6
size = width * length

i_2 = [[1,   1,  1,  1,  1,  1],     #2
     [ -1,  -1, -1, -1, -1,  1],     #
     [  1,   1,  1,  1,  1,  1],     #
     [  1,  -1, -1, -1, -1, -1],
     [  1,  -1, -1, -1, -1, -1],     #
     [  1,   1,  1,  1,  1,  1]]     #
                                     #
i_4 = [[1, -1, -1, -1, -1, 1],       #4
     [  1, -1, -1, -1, -1, 1],       #
     [  1,  1,  1,  1,  1, 1],       #
     [ -1, -1, -1, -1, -1, 1],       #
     [ -1, -1, -1, -1, -1, 1],       #   Эталоны
     [ -1, -1, -1, -1, -1, 1]]       #
                                     #
i_8 = [[1,  1,  1,  1,  1,  1],      #8
     [  1, -1, -1, -1, -1,  1],      #
     [  1,  1,  1,  1,  1,  1],      #
     [  1, -1, -1, -1, -1,  1],      #
     [  1, -1, -1, -1, -1,  1],      #
     [  1,  1,  1,  1,  1,  1]]      #

def vectorize(X, arr):
    """

    :rtype : object
    """
    for i in range(length):
        for j in range(width):
            X.append(arr[i][j])


def setWeigthRNS(W, X, size):
    for i in range(size):
        for j in range(size):
            W[i][j] += X[i] * X[j]


def activateFunc(W, X, distortedArr, size, arr, countOfRecursion):
    countOfRecursion += 1
    if countOfRecursion > 10:
        return False

    for i in range(size):
        arr.append(distortedArr[i])

    for i in range(size):
        net = 0
        for j in range(size):
            net += arr[j] * W[j][i]
        if net > 0:
            distortedArr[i] = 1
        elif net < 0:
            distortedArr[i] = -1
    for i in range(size):
        if distortedArr[i] != X[i]:
            activateFunc(W, X, distortedArr, size, [], countOfRecursion)


vectors = []
for i in range(3):
    vectors.append([])

vectorize(vectors[0], i_2)
vectorize(vectors[1], i_4)
vectorize(vectors[2], i_8)

W = [0] * size
for i in range(size):
    W[i] = [0] * size

setWeigthRNS(W, vectors[0], size)
setWeigthRNS(W, vectors[1], size)
setWeigthRNS(W, vectors[2], size)

for i in range(size):
    W[i][i] = 0

distortedArr = []
for i in range(3):
    distortedArr.append([])

for i in range(size):
    distortedArr[0].append(vectors[0][i])

for i in range(size):
    distortedArr[1].append(vectors[1][i])

for i in range(size):
    distortedArr[2].append(vectors[2][i])

# следующая часть - проверка программы на эталонных образцах
flag1 = activateFunc(W, vectors[0], vectors[0], size, [], 0)
flag2 = activateFunc(W, vectors[1], vectors[1], size, [], 0)
flag3 = activateFunc(W, vectors[2], vectors[2], size, [], 0)

if flag1 == False:
    print("Распознать первый эталонный образец не удалось")
else:
    print("Первый эталонный образец распознан")

if flag2 == False:
    print("Распознать второй эталонный образец не удалось")
else:
    print("Второй эталонный образец распознан")

if flag3 == False:
    print("Распознать третий эталонный образец не удалось")
else:
    print("Третий эталонный образец распознан")

#последовательное изменение всех трех образцов и восстановление из них

for num in range(3):
    print("Изменяем образец номер ", num + 1)
    print("Введите номера пикселей (0..14), которые хотите изменить. \n(Для завершения процесса искажения введите число за пределом [0,14]):\n>>>")
    a = input()
    a = int(a)
    while (a > -1) & (a < 14):
        if distortedArr[num][a] == -1:
            distortedArr[num][a] = 1
        else:
            distortedArr[num][a] = -1
        a = input()
        a = int(a)

    flag = activateFunc(W, vectors[num], distortedArr[num], size, [], 0)

    if flag == False:
        print("Распознать эталон не удалось")
    else:
        i = 0
        while i < 36:
            print(distortedArr[num][i:i + 6])
            i += 6
        mayBe = [1, 1, 1]

        for i in range(size):
            if distortedArr[num][i] != vectors[0][i]:
                mayBe[0] = 0
            if distortedArr[num][i] != vectors[1][i]:
                mayBe[1] = 0
            if distortedArr[num][i] != vectors[2][i]:
                mayBe[2] = 0

        for i in range(3):
            if mayBe[i] == 1:
                print("Распознан образец #", i + 1)
            else:
                print("Распознать образец # %i не удалось" %(i + 1))