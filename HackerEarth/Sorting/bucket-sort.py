def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

def countSetBits(val: int) -> int:
    count = 0

    while val != 0:
        val = val & (val-1)
        count += 1

    return count

def bucketSort(array):
    buckets = [[] for i in range(10)]

    for val in array:
        buckets[countSetBits(val)].append(val)

    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])

    return buckets

def solve():
    readInt()
    array = readIntArray()

    buckets = bucketSort(array)
    for bucket in buckets:
        if len(bucket) > 0:
            print(" ".join([str(x) for x in bucket]))

solve()
