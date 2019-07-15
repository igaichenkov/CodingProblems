def readIntArray():
    res = []
    for val in input().split():
        res.append(int(val))
    return res

def readInt():
    return int(input())

def merge(arr, start, mid, end) -> int:
    leftPosition = start
    rightPosition = mid+1

    mergedArray = []
    leftIsBiggerCnt = 0

    while leftPosition <= mid or rightPosition <= end:
        if leftPosition > mid:
            mergedArray.append(arr[rightPosition])
            rightPosition += 1
        elif rightPosition > end:
            mergedArray.append(arr[leftPosition])
            leftPosition += 1
        elif arr[leftPosition] <= arr[rightPosition]:
            mergedArray.append(arr[leftPosition])
            leftPosition += 1
        else:
            mergedArray.append(arr[rightPosition])
            rightPosition += 1
            # left half is already sorted, therefore, if the current number from the left half
            # if bigger the right one, every further number until the mid is also bigger then the
            # current right half's number
            leftIsBiggerCnt += mid - leftPosition + 1 

    for i in range(start, end + 1):
        arr[i] = mergedArray[i - start]

    return leftIsBiggerCnt

def split(arr, start, end) -> int:
    if start == end:
        return 0

    leftIsBiggerCnt = 0

    mid = int((start + end) / 2)
    leftIsBiggerCnt += split(arr, start, mid)
    leftIsBiggerCnt += split(arr, mid + 1, end)

    leftIsBiggerCnt += merge(arr, start, mid, end)
    return leftIsBiggerCnt

def mergeSort(arr):
    return split(arr, 0, len(arr) - 1)

arraySize = readInt()
arr = readIntArray()
print(mergeSort(arr))