""""
    Returns: the list of integer converted in binary from 1 to n
    Parameters: n is the number that decides the interval
    Precondition: n is int, n > 0
    Return type: list of integers
    Complexity: O(n * log n)
"""
def getValues(n):
    l = []
    for nr in range(1, n + 1):
        l.append(int("{0:b}".format(nr)))
    return l

def tests():
    n1 = 4
    n2 = 6
    n3 = 1
    assert getValues(n1) == [1, 10, 11, 100]
    assert getValues(n2) == [1, 10, 11, 100, 101, 110]
    assert getValues(n3) == [1]

def main():
    tests()
    n = int(input("Introduceti n: "))
    print(getValues(n))

main()