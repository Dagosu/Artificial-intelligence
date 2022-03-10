""""
    Returns: last alphabetical word
    Parameter textString: the text in which we look for the word
    Precondition: textString is a string
    Return type: string
    Complexity: O(n)
"""
def getWord(textString):
    if len(textString) == 0:
        return ""

    wordsList = textString.split()
    finalWord = wordsList[0]
    for w in wordsList[1:len(wordsList)]:
        if w > finalWord:
            finalWord = w
    return finalWord

def tests():
    text1 = "Ana are mere si pere"
    text2 = "zzz fdsf gfdsg df"
    text3 = ""
    text4 = "da da dap"
    text5 = "a b c d"
    text6 = "test"
    assert getWord(text1) == "si"
    assert getWord(text2) == "zzz"
    assert getWord(text3) == ""
    assert getWord(text4) == "dap"
    assert getWord(text5) == "d"
    assert getWord(text6) == "test"

def main():
    tests()
    s = input()
    print(getWord(s))

main()
