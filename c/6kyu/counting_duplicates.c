/*
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and 
numeric digits that occur more than once in the input string. The input string can be assumed to 
contain only alphabets (both uppercase and lowercase) and numeric digits.
*/

def duplicate_count(text):
    # convert text to all lowercase alphanumeric & populate list of characters in text
    text = text.lower()
    chars = list(text)
    
    # create list "nodupes" containing one instance of each character that appears in "chars"
    nodupes = []
    for c in chars:
        if c not in nodupes:
            nodupes.append(c)
            
    # for each character in "nodupes", increment duplicate count by 1 if duplicate() returns True
    duplicates = 0
    for c in nodupes:
        if duplicate(chars, c) == True:
            duplicates += 1
    
    # return final count of duplicates
    return duplicates

def duplicate(chars, x):
    # increment n by 1 each time x appears in original list of characters including duplicates
    n = 0
    for c in chars:
        if c == x:
            n += 1
            
    # if x appears in chars 2 or more times, return True, otherwise return False
    if n >= 2:
        return True
    else:
        return False
