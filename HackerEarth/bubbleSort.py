def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

n = readInt()
arr = readIntArray()
swapsCount = 0

for i in range(n):
    for j in range(n-1, i, -1):
        if arr[j] < arr[j-1]:
            tmp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = tmp

            swapsCount += 1

print(swapsCount)