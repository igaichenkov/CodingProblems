import sys

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

def swap(arr, index1, index2):
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp

def sort(arr, maxSteps):
    maxSteps = min(maxSteps, len(arr)-1)
    for i in range(maxSteps):
        minPos = i

        for j in range(i+1, len(arr)):
            if (arr[minPos] > arr[j]):
                minPos = j

        if minPos == i:
            continue

        swap(arr, i, minPos)

arrayLen, maxIterations = readIntArray()
arr = readIntArray()
sort(arr, maxIterations)
print(" ".join([str(x) for x in arr]))