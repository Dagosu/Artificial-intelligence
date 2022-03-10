class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def getFirst(self):
        return self.first

    def getSecond(self):
        return self.second

""""
    Returns: the matrix of partial sums of the inital matrix
    Parameters: n is the number of rows
                m is the number of columns
                matrix is the matrix of integers
    Precondition: n is int, n > 0
                  m is int, m > 0
                  matrix is matrix of integers
    Return type: matrix of integers
    Complexity: O(n ^ 2)
"""
def buildPartialSumsMatrix(n, m, matrix):
    partialSums = []
    for i in range(n):
        partialSums.append([])
        for j in range(m):
            partialSums[i].append(matrix[i][j])
            if i - 1 >= 0:
                partialSums[i][j] += partialSums[i - 1][j]
            if j - 1 >= 0:
                partialSums[i][j] += partialSums[i][j - 1]
            if  i - 1 >= 0 and j - 1 >= 0:
                partialSums[i][j] -= partialSums[i - 1][j - 1]
    return partialSums

""""
    Returns: the sums indicated by the pairs of points
    Parameters: n is the number of rows
                m is the number of columns
                matrix is the matrix of integers
                pairs is the pairs of points
    Precondition: n is int, n > 0
                  m is int, m > 0
                  matrix is matrix of integers
                  pairs is a list of Pairs
    Return type: list of integers
    Complexity: O(n)
"""
def getSums(n, m, matrix, pairs):
    partialSums = buildPartialSumsMatrix(n, m, matrix)
    sums = []
    for pair in pairs:
        a = pair.getFirst()
        b = pair.getSecond()
        sum = partialSums[b.getX()][b.getY()]
        if a.getY() - 1 >= 0:
            sum -= partialSums[b.getX()][a.getY() - 1]
        if a.getX() - 1 >= 0:
            sum -= partialSums[a.getX() - 1][b.getY()]
        if a.getX() - 1 >= 0 and a.getY() - 1 >= 0:
            sum += partialSums[a.getX() - 1][a.getY() - 1]
        sums.append(sum)
    return sums

def tests():
    n = 5
    m = 5
    matrix = [[0, 2, 5, 4, 1], [4, 8, 2, 3, 7], [6, 3, 4, 6, 2], [7, 3, 1, 8, 3], [1, 5, 7, 9, 4]]
    pairs1 = [Pair(Point(1, 1), Point(3, 3)), Pair(Point(2, 2), Point(4, 4))]
    pairs2 = [Pair(Point(0, 0), Point(4, 4))]
    assert getSums(n, m, matrix, pairs1) == [38, 44]
    assert getSums(n, m, matrix, pairs2) == [105]

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
    k = int(input("Introduceti numarul de perechi: "))
    pairs = []
    for i in range(k):
        s = input()
        s = s.split()
        x1 = int(s[0])
        y1 = int(s[1])
        x2 = int(s[2])
        y2 = int(s[3])
        pair = Pair(Point(x1, y1), Point(x2, y2))
        pairs.append(pair)
    return n, m, matrix, pairs

def main():
    tests()
    n, m, matrix, pairs = readUserInput()
    print(getSums(n, m, matrix, pairs))

main()