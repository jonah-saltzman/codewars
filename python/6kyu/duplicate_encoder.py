# The goal of this exercise is to convert a string to a new string 
# where each character in the new string is "(" if that character 
# appears only once in the original string, or ")" if that character 
# appears more than once in the original string. Ignore capitalization 
# when determining if a character is a duplicate.

def duplicate_encode(word):
    word = word.lower()
    chars = list(word)
    array = []
    for c in word:
        count = 0
        for element in chars:
            if c == element:
                count += 1
        if count == 1:
            array.append("(")
        else:
            array.append(")")
    string = ""
    for c in array:
        string += c
    return string
