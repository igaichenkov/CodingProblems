class Graph:
    def __init__(self, verticesCount):
        self.__edges = [[] for i in range(verticesCount)]
        self.__verticesCount = verticesCount
        self.__time = 0

    def addEdge(self, fromVertex, toVertex):
        self.__edges[fromVertex].append(toVertex)

    def __dfs(self, at, inStack, inStackCount):
        if inStackCount == self.__verticesCount:
            return True

        for to in self.__edges[at]:
            inStack[to] = True

            if self.__dfs(to, inStack, inStackCount + 1):
                return True

            inStack[to] = False

        return False

    def containsHamiltonianPath(self):
        inStack = [False for i in range(self.__verticesCount)]

        for vertex in range(self.__verticesCount):
            inStack[vertex] = True

            if self.__dfs(vertex, inStack, 0):
                return True

            inStack[vertex] = False

        return False

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

verticesCount, edgesCount = readIntArray()
graph = Graph(verticesCount)

for i in range(edgesCount):
    fromVertex, toVertex = readIntArray()
    graph.addEdge(fromVertex, toVertex)

if graph.containsHamiltonianPath():
    print("YES")
else:
    print("NO")