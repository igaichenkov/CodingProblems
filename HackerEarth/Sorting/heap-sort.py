import copy

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

class Heap:

    def __init__(self):
        self.__heapData = []

    def __getParentIndex(self, currentIndex):
        return int((currentIndex - 1) / 2)

    def __getLeftChild(self, parentIndex):
        return parentIndex * 2 + 1

    def __getRightChild(self, parentIndex):
        return parentIndex * 2 + 2

    def __swap(self, index1, index2):
        self.__heapData[index1], self.__heapData[index2] = self.__heapData[index2], self.__heapData[index1]

    def __trickleUp(self, index):
        if index == 0:
            return 0

        parentIndex = self.__getParentIndex(index)

        while index > 0 and self.__heapData[parentIndex] > self.__heapData[index]:
            self.__swap(parentIndex, index)
            index = parentIndex
            parentIndex = self.__getParentIndex(index)

    def __getMinValueIndex(self, index1: int, index2: int) -> int:
        val1, val2 = self.__heapData[index1], self.__heapData[index2]

        if val1 > val2:
            return index2

        return index1

    def __trickleDown(self, index):
        leftIndex = self.__getLeftChild(index)
        rightIndex = self.__getRightChild(index)

        arrayLen = len(self.__heapData)
        lastPosition = arrayLen - 1

        while rightIndex <= arrayLen:
            if leftIndex == lastPosition:
                if self.__heapData[leftIndex] < self.__heapData[index]:
                    self.__swap(leftIndex, index)
                    index = leftIndex
                
                break

            minChildIndex = self.__getMinValueIndex(leftIndex, rightIndex)
            self.__swap(index, minChildIndex)
            
            index = minChildIndex
            leftIndex = self.__getLeftChild(index)
            rightIndex = self.__getRightChild(index)

    def add(self, value):
        if len(self.__heapData) == 0:
            self.__heapData.append(value)
            return

        self.__heapData.append(value)
        itemIndex = len(self.__heapData) - 1
        self.__trickleUp(itemIndex)
    
    def remove(self) -> int:
        rootValue = self.__heapData[0]

        if len(self.__heapData) == 1:
            self.__heapData.pop()
            return rootValue

        self.__heapData[0] = self.__heapData.pop()
        self.__trickleDown(0)

        return rootValue

    def getCount(self) -> int:
        return len(self.__heapData)

    def getTopN(self, count):
        return self.__heapData[:count]

    def replaceRoot(self, newRoot):
        self.__heapData[0] = newRoot
        self.__trickleDown(0)

    def getRoot(self) -> int:
        return self.__heapData[0]

def solve():
    TOPN = 3

    count = readInt()

    heap = Heap()

    for _ in range(count):
        value = readInt()
        heap.add(value)
        
        if heap.getCount() < TOPN:
            print(-1)
            continue

        if heap.getCount() == TOPN+1:
            heap.remove()

        currentTop = []
        for _ in range(TOPN):
            currentTop.append(heap.remove())

        print(" ".join([str(x) for x in reversed(currentTop)]))
        for val in currentTop:
            heap.add(val)

solve()