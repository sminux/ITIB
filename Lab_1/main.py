'''
Created on 2 апр. 2017 г.

@author: Сергей
'''
import functions

print('ITIB Laboratory work #1. Investigation of single-layer neural networks by example Simulation of boolean expressions')

for inc in range(2):
    print('AF ', inc + 1 , ': ')
    af = inc
    functions.learning(inc)
    print('________________________________________________')

print('Learning on min sets: ')
functions.learning_sets()
print('________________________________________________')