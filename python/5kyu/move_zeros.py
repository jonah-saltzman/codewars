# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    zeros = 0
    print(array)
    for i in range(len(array)):
        if array[i] == 0:
            zeros += 1
    for i in range(zeros):
        array.remove(0)
    for i in range(zeros):
        array.append(0)
    return(array)
