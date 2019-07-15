def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

def countingSort(array):
    freq = [0 for i in range(len(array))]

    for val in array:
        freq[val-1] += 1

    return freq

def solve():
    readInt()
    array = readIntArray()

    freq = countingSort(array)

    for i in range(len(freq)):
        if (freq[i] == 0):
            continue

        print(i+1, freq[i])

solve()