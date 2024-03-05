# MARCO CERBELLA RLE COMPRESSION
 
from random import choice
 
colors = ['b', 'r', 'v', 'g']
MATRIX_LEN = [5, 5] # cols / rows
MATRIX_W = MATRIX_LEN[0]*MATRIX_LEN[1]*24
 
def getMatrix():
    return [[choice(colors) for x in range(MATRIX_LEN[0])] for j in range(MATRIX_LEN[1])]
    # genera matrice di lettere casuali
 
def codec(matrix):
    return [{i:x.count(i) for i in x} for x in matrix]
    # conta le ricorrenze dei colori in una lista di dizionari (1 diz. per riga) es. [ {'b':2, 'v':1}, {'r':1, 'b': 2}, etc... ]
 
def getBinLen(n):
    return len(bin(n).replace('0b', ''))
    # restituisce lo spazio necessario per rappresentare n in binario
 
 
matrix = getMatrix()
set_matrix = codec(matrix)
final_w = 0
 
for y in set_matrix:
    sum = 0
    for j in y.keys():
        sum += 24+getBinLen(y[j]) 
 
    final_w+=sum
 
CP = round(100-final_w/MATRIX_W*100, 2)
 
print(f'MATRIX: {MATRIX_W} bit\n')
for i in matrix:
    print(i)
 
print(f'\nCOMPRESSED: {final_w} bit\nComp/rate: {CP}%')
