def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

def countingSort(array, divider):
    RADIX = 10
    freq = [0 for i in range(RADIX)]
    output = [0 for i in range(len(array))]

    for val in array:
        digit = int(val / divider) % RADIX
        freq[digit] += 1

    for i in range(1, RADIX):
        freq[i] += freq[i - 1]

    for i in range(len(array) - 1, -1, -1):
        digit = int(array[i] / divider) % RADIX
        index = freq[digit] - 1
        output[index] = array[i]

        freq[digit] -= 1

    for i in range(len(array)):
        array[i] = output[i]

def printArray(array):
    print(" ".join([str(x) for x in array]))

def radixSort(array):
    maxVal = max(array)
    divider = 1

    while maxVal > 0:
        countingSort(array, divider)
        divider *= 10
        maxVal = int(maxVal / 10)

        printArray(array)

def solve():
    readInt()
    array = readIntArray()

    radixSort(array)

solve()