def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

def quickSort(array, fromIndex, toIndex):
    if fromIndex >= toIndex:
        return
    
    pivotValue = array[toIndex]
    counter = fromIndex

    for i in range(fromIndex, toIndex):
        if array[i] < pivotValue:
            array[counter], array[i] = array[i], array[counter]
            counter += 1

    array[counter], array[toIndex] = array[toIndex], array[counter]

    quickSort(array, fromIndex, counter - 1)
    quickSort(array, counter + 1, toIndex)

def solve():
    arraySize = readInt()
    array = readIntArray()

    quickSort(array, 0, arraySize - 1)
    print(" ".join([str(x) for x in array]))

solve()