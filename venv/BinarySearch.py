import numpy as np

list = np.arange(3,30000,1)
print(list)
marked_element = 3**7

def findElementIndex(marked_element,list, low, high):
    mid = int((high+low)/2)
    if high < low:
        print("Element not found")
        return
    if marked_element == list[mid]:
        print("Element index: ",mid)
    elif marked_element < list[mid]:
        findElementIndex(marked_element,list,low,mid-1)
    else:
        findElementIndex(marked_element, list,mid+1,high)

findElementIndex(marked_element,list,0,len(list)-1)