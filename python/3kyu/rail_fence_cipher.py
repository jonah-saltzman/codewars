# Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a string by placing each 
# character successively in a diagonal along a set of "rails". First start off moving diagonally and down. When you reach the bottom, reverse 
# direction and move diagonally and up until you reach the top rail. Continue until you reach the end of the string. Each "rail" is then read 
# left to right to derive the encoded string.
#
# For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:
#
# W       E       C       R       L       T       E
#   E   R   D   S   O   E   E   F   E   A   O   C  
#     A       I       V       D       E       N    
#
# The encoded string would be:
#
# WECRLTEERDSOEEFEAOCAIVDEN
#
# Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.
#
# Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the DECODED string.
#
# For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.
#
# Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that include punctuation. 
# Don't filter out punctuation as they are a part of the string.
#
# https://www.codewars.com/kata/58c5577d61aefcf3ff000081


# encoder function
def encode_rail_fence_cipher(string, n):
  
    # create list rails containing a number of lists equal to the number of rails
    # fill each list in rails with a number of Nones equal to the length of the string
    LENGTH = len(string)
    rails = []
    for i in range(n):
        rails.append([])
        for _ in range(LENGTH):
            rails[i].append(None)
    
    # for each character in string, add the character to the current index of the current
    # rail; then, move the index to the right and move to the next rail, according to 
    # the direction variable. if the current rail is a fence, first reverse direction.
    rail = 0
    direction = "down"
    index = 0
    for c in string:
        rails[rail][index] = c
        index += 1
        if direction == "down":
            if rail == n - 1:
                rail -= 1
                direction = "up"
            else:
                rail += 1
        elif direction == "up":
            if rail == 0:
                rail += 1
                direction = "down"
            else:
                rail -= 1
    
    # to produce encoded string, move along the rails, left to right & top to bottom,
    # adding any truthy values to string.
    string = ""
    for i in range(n):
        for j in range(LENGTH):
            if rails[i][j]:
                string += rails[i][j]
    return string

def decode_rail_fence_cipher(string, n):
    
    # initialize rails exactly as in the encoder function
    LENGTH = len(string)
    rails = []
    for i in range(n):
        rails.append([])
        for _ in range(LENGTH):
            rails[i].append(None)
    
    # replace None with 1 according to the same pattern that would be used to encode a string
    rail = 0
    direction = "down"
    index = 0
    for _ in range(len(string)):
        rails[rail][index] = 1
        index += 1
        if direction == "down":
            if rail == n - 1:
                rail -= 1
                direction = "up"
            else:
                rail += 1
        elif direction == "up":
            if rail == 0:
                rail += 1
                direction = "down"
            else:
                rail -= 1

    # replace 1s with characters of encoded string, moving left to right
    # and top to bottom, skipping falsy values. this produces the same
    # set of rails used to produce encoded string.
    rail = 0
    rail_index = 0
    string_index = 0
    while True:
        if rail_index == LENGTH and rail < n:
            rail += 1
            rail_index = 0
        if string_index == LENGTH:
            break
        if rails[rail][rail_index]:
            rails[rail][rail_index] = string[string_index]
            rail_index += 1
            string_index += 1
        else:
            rail_index += 1

    # add values from rails to decoded string, moving in same zig-zag
    # pattern used to produce encoded string.
    rail = 0
    direction = "down"
    index = 0
    string = ""
    for _ in range(LENGTH):
        string += rails[rail][index]
        index += 1
        if direction == "down":
            if rail == n - 1:
                rail -= 1
                direction = "up"
            else:
                rail += 1
        elif direction == "up":
            if rail == 0:
                rail += 1
                direction = "down"
            else:
                rail -= 1
    return string
