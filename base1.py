import numpy as np
from math import sqrt

index = 0
resultarray = []
toparray = []
matrixA = np.zeros((12, 12), 'Float16')
matrixB = np.zeros((12, 12), 'Float16')
matrixC = np.zeros((12, 12), 'Float16')
swarList = ['Sa', 'Re', 'Ga', 'Ma', 'Pa', 'Dha', 'Ni', 're', 'ga', 'MA', 'dha', 'ni']
baseSetA = {'Sa': [], 'Re': [], 'Ga': [], 'Ma': [], 'Pa': [], 'Dha': [], 'Ni': [], 're': [], 'ga': [], 'MA': [],
            'dha': [], 'ni': []}
baseSetB = {'Sa': [], 'Re': [], 'Ga': [], 'Ma': [], 'Pa': [], 'Dha': [], 'Ni': [], 're': [], 'ga': [], 'MA': [],
            'dha': [], 'ni': []}
FILEPATH = './Ankush/notes'

def printDict(baseSet):
    for i in baseSet:
        if len(baseSet[i]) > 1:
            print (i)
            for j in baseSet[i][:-1]:
                print (j)


def probability(matrix):
    sum = 0
    for i in range(0, 12):
        sum = 0
        for j in range(0, 12):  # To Find The Sum of the Row
            sum += matrix[i][j]
        for j in range(0, 12):  # To Divide each Row with Sum
            if sum != 0:
                matrix[i][j] /= sum
    return matrix


def inputMatrix(matrix, baseSet, ch):
    index = 0
    filename = FILEPATH + str(ch) + ".txt"
    file = open(filename, 'r')
    for swar in file.read().split():
        if index == 0:
            temp = swar
        else:
            matrix[swarList.index(temp)][swarList.index(swar)] += 1
            temp = swar

        # For Finding Difference between two Consecutive Swar
        for i in baseSet:
            if swar == i:
                if len(baseSet[i]) == 0:
                    baseSet[i].append(index)
                else:
                    x = baseSet[i].pop(-1)
                    baseSet[i].append(index - x - 1)
                    baseSet[i].append(index)
        index += 1
    #printDict(baseSet)
    return matrix


print ("Welcome!")
choice = raw_input("Enter the number from 1 to 29:")
for i1 in range(1, 29):
    matrixA = probability(inputMatrix(matrixA, baseSetA, i1))
    matrixB = probability(inputMatrix(matrixB, baseSetB, choice))
    matrixC = np.subtract(matrixA, matrixB)
    matrixA = np.zeros((12, 12), 'Float16')
    matrixB = np.zeros((12, 12), 'Float16')
    trace = np.trace(np.dot(np.transpose(matrixC), matrixC))
    matrixC = np.zeros((12, 12), 'Float16')
    print ("The Trace is:" + str(trace) + "\t\t\t\tDistance is:" + str(sqrt(trace)))
    resultarray.append(sqrt(trace))
    toparray.append(sqrt(trace))

resultarray.sort()
for x in range(0, 3):
    print (str(resultarray[x]) + "\t\tSong No.:" + str(toparray.index(resultarray[x]) + 1))
