""""
    Returns: the number which appears exactly twice in the array
    Parameters: array is the given array of numbers
    Precondition: array is an array of numbers in which a single value is repeated twice
    Return type: int
    Complexity: O(n * log n)
"""
def getValue(array):
    if len(array) == 2 and array[0] == array[1]:
        return array[0]
    if array[0] == array[1] and array[1] != array[2]:
        return array[0]
    if array[len(array) - 1] == array[len(array) - 2] and array[len(array) - 2] != array[len(array) - 3]:
        return array[len(array) - 1]
    array.sort()
    for i in range(1, len(array) - 2):
        if array[i] == array[i + 1] and array[i] != array[i - 1] and array[i + 1] != array[i + 2]:
            return array[i]
    return


def tests():
    array1 = [1, 2, 3, 4, 2]
    array2 = [1, 1]
    array3 = [1, 2, 3, 4, 3, 10]
    assert getValue(array1) == 2
    assert getValue(array2) == 1
    assert getValue(array3) == 3

def main():
    tests()
    s = input()
    array = list(map(int, s.split()))
    print(getValue(array))

main()