import numpy as np
from math import sqrt

index = 0
LIMIT = 10
resultarray = []
toparray = []
matrixA = np.zeros((12, 144), 'Float16')
matrixB = np.zeros((12, 144), 'Float16')
matrixC = np.zeros((12, 12), 'Float16')
matrixtemp = np.zeros((12, 144), 'Float16')
swarList = ['Sa', 'Re', 'Ga', 'Ma', 'Pa', 'Dha', 'Ni', 're', 'ga', 'MA', 'dha', 'ni']
FILEPATH = './samples1/notes'
ragas = ['Bageshree', 'Bhimpalas', 'Bhup', 'Des', 'Durga', 'Kafi', 'Khamaj', 'Yaman', 'Yaman K']
resultragas = []

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
        for j in range(0, 144):  # To Find The Sum of the Row
            sum += matrix[i][j]
        for j in range(0, 144):  # To Divide each Row with Sum
            if sum != 0:
                matrix[i][j] /= sum
    return matrix


def inputMatrix(matrix, ch):
    index = 0
    filename = FILEPATH + str(ch) + ".txt"
    file = open(filename, 'r')
    for swar in file.read().split():
        if index == 0:
            temp1 = swar
        elif index == 1:
            temp2 = swar
        else:
            temp3 = swar
            col = swarList.index(temp1) * 12 + swarList.index(temp2)
            matrix[swarList.index(temp3)][col] += 1
            temp1 = temp2
            temp2 = temp3
        index = index + 1
    return matrix


print ("Welcome!")
# choice = raw_input("Enter the number from 1 to " + str(LIMIT) + ':')
for i1 in range(1, LIMIT+1):
    matrixA = probability(inputMatrix(matrixA, i1))
    matrixB = probability(inputMatrix(matrixB, 10))
    matrixC = np.subtract(matrixA, matrixB)
    matrixA = np.zeros((12, 144), 'Float16')
    matrixB = np.zeros((12, 144), 'Float16')
    trace = np.trace(np.dot(matrixC, np.transpose(matrixC)))
    matrixC = np.zeros((12, 12), 'Float16')
    # print ("The Trace is:" + str(trace) + "\t\t\t\tDistance is:" + str(sqrt(trace)))
    resultarray.append(sqrt(trace))
    toparray.append(sqrt(trace))

resultarray.sort()
print ("Distance\t\tSong No.")
for x in range(1, 10):
    print (str(resultarray[x]) + "\t\t" + str(toparray.index(resultarray[x])+1))

print ("First Best Match Raga:" + str(ragas[toparray.index(resultarray[1])]))
