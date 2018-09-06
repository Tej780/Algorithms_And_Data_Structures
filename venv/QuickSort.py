import numpy as np
from numpy import random

def quicksort(list,length):
    if length <=1:
        return list

    random_index = random.randint(0,length)
    random_marker = list[random_index]

    left = []
    right = []
    equal = []

    for i in range(len(list)):
        if list[i] < random_marker:
            left.append(list[i])
        elif list[i] == random_marker:
            equal.append(list[i])
        else:
            right.append(list[i])

    right = quicksort(right,len(right))
    left = quicksort(left,len(left))

    sortedList = left + equal + right
    return sortedList

unsortedList = [3,4,1,54,12,3,23,4]
print(quicksort(unsortedList,len(unsortedList)))

