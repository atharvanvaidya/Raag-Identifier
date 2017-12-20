import numpy as np
from math import sqrt

index = 0
matrixA = np.zeros((12, 12), 'Float16')
matrixB = np.zeros((12, 12), 'Float16')
matrixC = np.zeros((12, 12), 'Float16')
swarList = ['Sa', 'Re', 'Ga', 'Ma', 'Pa', 'Dha', 'Ni', 're', 'ga', 'MA', 'dha', 'ni']
baseSetA = {'Sa': [], 'Re': [], 'Ga': [], 'Ma': [], 'Pa': [], 'Dha': [], 'Ni': [], 're': [], 'ga': [], 'MA': [],
            'dha': [], 'ni': []}
baseSetB = {'Sa': [], 'Re': [], 'Ga': [], 'Ma': [], 'Pa': [], 'Dha': [], 'Ni': [], 're': [], 'ga': [], 'MA': [],
            'dha': [], 'ni': []}

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


def inputMatrix(matrix, baseSet):
    index = 0
    while 1:
        swar = raw_input()
        if index == 0:
            temp = swar
        else:
            if swar == 'exit':
                break
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
    printDict(baseSet)
    return matrix


print ("Welcome!")
print ("Type \"exit\" to Enter Soor of Song B.")
print ("Enter the Soor of Song A:")

matrixA = probability(inputMatrix(matrixA, baseSetA))
print ("Matrix A")
print (matrixA)

print ("Type \"exit\" to Display Trace and Distance.")
print ("Enter the Soor of Song B:")

matrixB = probability(inputMatrix(matrixB, baseSetB))
print ("Matrix B")
print (matrixB)

matrixC = np.subtract(matrixA, matrixB)
trace = np.trace(np.dot(np.transpose(matrixC), matrixC))
print ("The Trace is:" + str(trace))
print ("Distance is:" + str(sqrt(trace)))




