class Graph:
    def __init__(self, verticesCount):
        self.__edges = [[] for i in range(verticesCount)]
        self.__verticesCount = verticesCount
        self.__time = 0

    def addEdge(self, fromVertex, toVertex):
        self.__edges[fromVertex].append(toVertex)

    def __sortEdges(self):
        for vertex in range(self.__verticesCount):
            self.__edges[vertex] = sorted(self.__edges[vertex], reverse=True)

    def __dfs(self, at, verticesStack, visited):
        if visited[at]:
            return

        visited[at] = True
        for to in self.__edges[at]:
            self.__dfs(to, verticesStack, visited)

        verticesStack.append(at)

    def topologicalSort(self):
        visited = [False for i in range(self.__verticesCount)]
        verticesStack = []

        self.__sortEdges()
        for vertex in range(self.__verticesCount-1, -1, -1):
            self.__dfs(vertex, verticesStack, visited)
        
        return reversed(verticesStack)

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

verticesCount, edgesCount = readIntArray()
graph = Graph(verticesCount)

for i in range(edgesCount):
    fromVertex, toVertex = readIntArray()
    graph.addEdge(fromVertex-1, toVertex-1)

vertices = graph.topologicalSort()
print(" ".join(list(map(lambda x: str(x+1), vertices))))