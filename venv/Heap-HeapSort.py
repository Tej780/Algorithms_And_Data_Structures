def FindLeftChild(givenNodeIndex,tree):
    leftChild = tree[2*givenNodeIndex-1]
    return leftChild

def FindRightChild(givenNodeIndex,tree):
    rightChild = tree[2*givenNodeIndex]
    return rightChild

def FindParent(givenNodeIndex,tree):
    parentIndex = givenNodeIndex//2 - 1
    if parentIndex == -1:
        print("The root has no parents")
    else:
        parent = tree[parentIndex]
        return parent

def Swap(tree,node1Index,node2Index):
    tree[node1Index] = tree[node1Index] + tree[node2Index]
    tree[node2Index] = tree[node1Index] - tree[node2Index]
    tree[node1Index] = tree[node1Index] - tree[node2Index]
    return tree

def Sink(tree,k):
    length = len(tree)
    while 2*k <= length:
        smallest = 2*k
        if smallest < length and tree[2*k-1] > tree[2*k]:
            smallest = 2*k+1
        if tree[k-1] < tree[smallest-1]:
            break
        tree = Swap(tree,k-1,smallest-1)
        k = smallest
    return tree

def ExtractMin(tree):
    minimum = tree[0]
    tree[0] = tree[-1]
    tree.pop()
    tree = Sink(tree,1)
    return minimum,tree


def Swim(tree,k):
    while k > 1 and tree[k//2]>tree[k]:
        Swap(tree,k,k//2)
        k = k//2+1
    return tree

def Insert(tree,val):
    tree.append(val)
    tree = Swim(tree,len(tree)-1)
    return tree


def HeapSort(tree):
    sortedArray = []
    for i in range(len(tree)):
        minimum,tree = ExtractMin(tree)
        sortedArray.append(minimum)
    return sortedArray

tree = [2,3,6,7,10,8]
minimum,tree = ExtractMin(tree)
print(tree)
tree = Insert(tree,4)
print(tree)
print(HeapSort(tree))

