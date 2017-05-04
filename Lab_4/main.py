'''
Created on 2 мая 2017 г.

@author: Сергей
'''
#import matplotlib
'''
from pylab import *
from PIL import Image

def getArray(file):
    arr = [0]*36
    im = array(Image.open(file)) #проверяем последний цвет каждого элемента массива
    for i in range(width):
        for j in range(length):
            let = im[i][j]
            if let[-1] == 0:
                arr[i*width + j] = -1
            else:
                arr[i*width + j] = 1
    return arr
                
ideal = [[]]*3
ideal[0] = getArray('circle.png') 
ideal[1] = getArray('arc.png') 
ideal[2] = getArray('loop.png') 


x = [1,1,4,4] 
y = [2,3,2,3] 
plot(x,y,'r*') 
plot(x[:2],y[:2])  

axis('off')
imshow(im)
show()
'''


width = 6
length = 6
dim = width * length

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

def getVector(X, arr):  # преобразуем входной двумерный массив в вектор
    """
    :rtype : object
    """
    for i in range(length):
        for j in range(width):
            X.append(arr[i][j])


def getWeigth(W, X):        #функция вычисляющая матрицу весов W = X*Xтанспозир.
    for i in range(dim):
        for j in range(dim):
            if i == j:
                W[i][j] = 0
            else:
                W[i][j] += X[i] * X[j]  


def NET(W, X, distortedArr, arr, countRec):
    countRec += 1
    if countRec > 16:
        return False

    for i in range(dim):
        arr.append(distortedArr[i])
    ''' 
    for i in range(dim):
        for j in range(dim):    
            print(W[i][j], end='')
        print()
    '''
    #правило Хебба (обучение за один такт)
    for i in range(dim):
        net = 0
        for j in range(dim):
            net += arr[j] * W[j][i]
        if net > 0:
            distortedArr[i] = 1
        elif net < 0:
            distortedArr[i] = -1
    for i in range(dim):
        if distortedArr[i] != X[i]:
            NET(W, X, distortedArr, [], countRec)


idol = []           #инициализируем эталоны и записываем их векторами
for i in range(3):
    idol.append([])
getVector(idol[0], i_2)
getVector(idol[1], i_4)
getVector(idol[2], i_8)

W = [0] * dim       #инициализируем матрицы весов
for i in range(dim):
    W[i] = [0] * dim
getWeigth(W, idol[0])
getWeigth(W, idol[1])
getWeigth(W, idol[2])

distortedArr = []
for i in range(3):
    distortedArr.append([])

for i in range(dim):
    distortedArr[0].append(idol[0][i])
for i in range(dim):
    distortedArr[1].append(idol[1][i])
for i in range(dim):
    distortedArr[2].append(idol[2][i])

#тест на эталонных образцах
check = [0] * dim
for i in range(dim):
    check[i] = [0] * dim

for i in range(3):
    check[i] = NET(W, idol[i], idol[i], [], 0)
    if check[i] == False:
        print("Распознать %i-й эталон образец не удалось" %(i + 1))
    else:
        print("Эталон #%i  распознан" %(i + 1))


#искажение эталонов и распознавание
for num in range(3):
    print("__________________________________________________")
    print("Изменяем эталон №_", num + 1, "_")
    print("Введите номера пикселей (0..35), которые хотите изменить. \n(Для завершения процесса искажения введите число за пределом [0, 35]):\n>>>")
    a = input()
    a = int(a)
    while (a > -1) & (a < 36):
        if distortedArr[num][a] == -1:
            distortedArr[num][a] = 1
        else:
            distortedArr[num][a] = -1
        a = input()
        a = int(a)
        
       
    ''' 
    for i in range(length):
        for j in range(width):
            print(distortedArr[num][i + j], end = ' ')
        print()
    '''  
    flag = NET(W, idol[num], distortedArr[num], [], 0)

    if flag == False:
        print("Распознать эталон не удалось")
    else:
        i = 0
        while i < 36:
            print(distortedArr[num][i:i + 6])     #берем со срезом
            i += 6
        probability = [1]*3             #вероятность распознавания

        for i in range(dim):
            if distortedArr[num][i] != idol[0][i]:
                probability[0] = 0
            if distortedArr[num][i] != idol[1][i]:
                probability[1] = 0
            if distortedArr[num][i] != idol[2][i]:
                probability[2] = 0

        for i in range(3):
            if probability[i] == 1:
                print("Распознан эталон #", i + 1)
            else:
                print("Распознать эталон # %i не удалось" %(i + 1))