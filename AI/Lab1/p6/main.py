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
    Returns: majority number if it exists,
             -1, if it does not exist
    Parameters: array is the given array of numbers
    Precondition: array is an array of numbers
    Return type: int
    Complexity: O(n)
"""
def getElement(array):
    finalNr = -1
    frequency = 0
    d = createDictionary(array)
    for nr in d:
        if d[nr] > len(array) / 2 and d[nr] > frequency:
            finalNr = nr
            frequency = d[nr]
    return finalNr


def tests():
    array1 = [2,8,7,2,2,5,2,3,1,2,2]
    array2 = [3, 3, 2, 3, 3, 2]
    array3 = [1, 1, 1]
    array4 = [2, 3, 4]
    assert getElement(array1) == 2
    assert getElement(array2) == 3
    assert getElement(array3) == 1
    assert getElement(array4) == -1

def main():
    tests()
    s = input("Introduceti sirul: ")
    e = getElement(list(map(int, s.split())))
    if e != -1:
        print(e)
    else:
        print("Nu exista niciun element majoritar")

main()