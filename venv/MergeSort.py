import numpy as np

def merge(list1,list2):
    i = j = 0
    list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list.append(list1[i])
            i+=1
        elif list1[i] > list2[j]:
            list.append(list2[j])
            j+=1
        else:
            list.append(list1[i])
            list.append(list2[j])
            i+=1
            j+=1
    while i < len(list1):
        list.append(list1[i])
        i+=1
    while j < len(list2):
        list.append(list2[j])
        j+=1
    return list

def mergesort(list):
    if len(list) <= 1:
        return list
    midpoint = len(list)//2

    leftSublist = mergesort(list[:midpoint])
    rightSublist = mergesort(list[midpoint:])
    sortedList = merge(leftSublist,rightSublist)
    return sortedList

unsortedArray = [16,14,13,16,24,56,8,123,42,1,4323,2,21,32,12,13,14]
print(mergesort(unsortedArray))