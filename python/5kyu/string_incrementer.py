# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

import re

def increment_string(string):
    # if string ends in digits, set digits to "digits"
    # otherwise return string concatenated with "1"
    digits = re.search(r'\d+$', string)
    if digits:
        digits = digits.group()
    else:
        return string + "1"

    # build "word" from all characters prior to trailing digits
    chars = len(string) - len(digits)
    word = ""
    for i in range(chars):
        word += string[i]

    # increment digits by 1; if resulting string is equal to or longer
    # than original length of trailing digits, simply concatenate string
    # of new digits to word. Otherwise, add leading zeros to "digits" 
    # before concatenating
    diglen = len(digits)
    digits = int(digits) + 1
    if len(str(digits)) < diglen:
        zeros = diglen - len(str(digits))
        zstring = "0" * zeros
        digits = zstring + str(digits)
    else:
        digits = str(digits)
    string = word + digits
    return string
