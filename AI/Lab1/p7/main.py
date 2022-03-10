""""
    Returns: the k'th biggest number in the list
    Parameters: array is the given array of numbers
                k is the k'th number we are looking for
    Precondition: array is an array of int
                  k is int
    Return type: int
    Complexity: O(n * log n)
"""
def getElement(array, k):
    array.sort(reverse=True)
    finalNr = array[0]
    k -= 1

    for i in range(1, len(array)):
        if k == 0:
            return finalNr
        if array[i] != array[i - 1]:
            k -= 1
            finalNr = array[i]

    return finalNr

def tests():
    array1 = [7, 4, 6, 3, 9, 1]
    array2 = [2, 3]
    assert getElement(array1, 2) == 7
    assert getElement(array1, 5) == 3
    assert getElement(array1, 1) == 9
    assert getElement(array2, 1) == 3

def main():
    tests()
    s = input("Introduceti sirul: ")
    k = int(input("Introduceti k: "))
    e = getElement(list(map(int, s.split())), k)
    print(e)

main()