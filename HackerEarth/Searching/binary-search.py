def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

class Solution:
    def __init__(self, arr):
        self.data = sorted(arr)

    def find(self, value):
        min = 0
        max = len(self.data)

        while min <= max:
            mid = int((min + max) / 2)

            if self.data[mid] == value:
                return mid

            if self.data[mid] < value:
                min = mid
            else:
                max = mid

        return -1


arrLen = readInt()
values = readIntArray()

solution = Solution(values)

queriesCount = readInt()
for i in range(queriesCount):
    query = readInt()
    print(solution.find(query) + 1)