""""
    Returns: list of words which appear only once in the given text
    Parameters: text is the given text string
    Precondition: text is string
    Return type: list of strings
    Complexity: O(n*log(n))
"""
def getWords(text):
    if text == "":
        return []

    finalWords = []
    wordsList = text.split()

    if len(wordsList) == 1:
        finalWords.append(wordsList[0])
        return finalWords

    wordsList.sort()

    if wordsList[0] != wordsList[1]:
        finalWords.append(wordsList[0])
    for i in range(1, len(wordsList) - 1):
        if wordsList[i] != wordsList[i - 1] and wordsList[i] != wordsList[i + 1]:
            finalWords.append(wordsList[i])
    if wordsList[len(wordsList) - 1] != wordsList[len(wordsList) - 2]:
        finalWords.append(wordsList[len(wordsList) - 1])

    return finalWords

def tests():
    text1 = "ana are ana are mere rosii ana"
    text2 = "a b c d"
    text3 = "a a b b"
    text4 = ""
    text5 = "a"
    text6 = "a b"
    assert getWords(text1) == ["mere", "rosii"]
    assert getWords(text2) == ["a", "b", "c", "d"]
    assert getWords(text3) == []
    assert getWords(text4) == []
    assert getWords(text5) == ["a"]
    assert getWords(text6) == ["a", "b"]

def main():
    tests()
    s = input()
    print(getWords(s))

main()