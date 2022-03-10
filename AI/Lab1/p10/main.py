""""
    Returns: the row's index which has the most 1's
    Parameters: n is the number of rows
                m is the number of columns
                matrix is the matrix of 1's and 0's
    Precondition: n is int, n > 0
                  m is int, m > 0
                  matrix is matrix of 1's and 0's
    Return type: int
    Complexity: O(n ^ 2)
"""
def getIndex(n, m, matrix):
    index = -1
    sumMax = 0
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += matrix[i][j]
        if sum > sumMax:
            index = i
            sumMax = sum
    return index

def tests():
    n = 3
    m = 5
    matrix1 = [[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]]
    matrix2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    matrix3 = [[0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]]
    assert getIndex(n, m, matrix1) == 1
    assert getIndex(n, m, matrix2) == -1
    assert getIndex(n, m, matrix3) == 0

def readUserInput():
    n = int(input("Introduceti n: "))
    m = int(input("Introduceti m: "))
    matrix = []
    for i in range(n):
        matrix.append([])
        s = input()
        s = s.split()
        for j in range(len(s)):
            matrix[i].append(int(s[j]))
    return n, m, matrix

def main():
    tests()
    n, m, matrix = readUserInput()
    index = getIndex(n, m, matrix)
    if index != -1:
        print(index)
    else:
        print("Nicio linie nu contine elemente de 1!")

main()
