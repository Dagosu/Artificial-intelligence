import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

""""
    Returns: distance between two points
    Parameters: a first Point, b second Point
    Precondition: a is Point, b is Point
    Return type: double
    Complexity: O(1)
"""
def getDistance(a, b):
    return math.sqrt((a.getX() - b.getX()) ** 2 + (a.getY() - b.getY()) ** 2)

def tests():
    a = Point(1, 5)
    b = Point(4, 1)
    c = Point(0, 0)
    d = Point(4, 0)
    assert getDistance(a, b) == 5.0
    assert getDistance(c, d) == 4.0

def readUserInput():
    s = input()
    s = s.split()
    a = Point(int(s[0]), int(s[1]))
    b = Point(int(s[2]), int(s[3]))
    return a, b

def main():
    tests()
    a, b = readUserInput()
    print(getDistance(a, b))

main()