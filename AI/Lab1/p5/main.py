""""
    Returns: dictionary of elements from the array and with their frequency
    Parameters: array is the given array of numbers
    Precondition: array is an array of numbers
    Return type: dictionary
    Complexity: O(n^2)
"""
def createDictionary(array):
    dict = {}
    for nr in array:
        if nr in dict.keys():
            dict[nr] += 1
        else:
            dict[nr] = 1
    return dict

""""
    Returns: the number which appears exactly twice in the array
    Parameters: array is the given array of numbers
    Precondition: array is an array of numbers in which a single value is repeated twice
    Return type: int
    Complexity: O(n)
"""
def getValue(array):
    dict = createDictionary(array)
    for nr in dict:
        if dict[nr] == 2:
            return nr
    return


def tests():
    array1 = [1, 2, 3, 4, 2]
    array2 = [1, 1]
    assert getValue(array1) == 2
    assert getValue(array2) == 1

def main():
    tests()
    s = input()
    array = list(map(int, s.split()))
    print(getValue(array))

main()