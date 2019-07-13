import copy

class InsertionSort:
    def __init__(self, arr):
        self.arr = copy.copy(arr)

    def getArrItem(self, positions, index):
        return self.arr[positions[index]]
        
    def sort(self):
        for i in range(len(self.arr)):
            j = i
            currentItemToInsert = self.arr[i]

            while j > 0 and currentItemToInsert < self.arr[j-1]:
                self.arr[j] = self.arr[j-1]
                j -= 1

            self.arr[j] = currentItemToInsert

        positionsMap = dict()
        for i in range(len(self.arr)):
            positionsMap[self.arr[i]] = i

        return positionsMap


def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

arraySize = readInt()
arr = readIntArray()

sortUtil = InsertionSort(arr)
positionsMap = sortUtil.sort()

print(" ".join([str(positionsMap.get(x) + 1) for x in arr]))