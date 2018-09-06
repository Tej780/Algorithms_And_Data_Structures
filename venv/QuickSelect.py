import numpy as np
from numpy import random

def quickselect(list,index):
    length = len(list)
    if length == 1:
        print(list[0])
        return

    random_index = random.randint(0,len(list)-1)
    random_marker = list[random_index]

    left = []
    right = []

    for i in range(len(list)):
        if not i == random_index:
            if list[i] <= random_marker:
                left.append(list[i])
            else:
                right.append(list[i])

    if index == len(left)+1:
        print(random_marker)
        return
    elif index <= len(left)+1:
        quickselect(left, index)
    else:
        quickselect(right,index-len(left)-1)


unsortedList = [3,4,1,54,12,3,23,4]
quickselect(unsortedList,6)

