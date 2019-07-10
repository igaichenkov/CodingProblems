class GraphAnalysis:
    def __init__(self, oddCompoonents, evenComponents):
        self.oddCompoonents = oddCompoonents
        self.evenComponents = evenComponents

class Graph:
    def __init__(self, verticesCount):
        self.__edges = [[] for i in range(verticesCount)]
        self.__verticesCount = verticesCount
        self.__time = 0

    def addEdge(self, fromVertex, toVertex):
        self.__edges[fromVertex].append(toVertex)

    def __reverseEdges(self):
        newEdges = [[] for i in range(len(self.__edges))]
        for fromVertex in range(len(self.__edges)):
            for toVertex in self.__edges[fromVertex]:
                newEdges[toVertex].append(fromVertex)

        self.__edges = newEdges

    def __traverseDfs(self, visited, at, verticesStack):
        if visited[at]:
            return

        visited[at] = True
        for to in self.__edges[at]:
            self.__traverseDfs(visited, to, verticesStack)

        verticesStack.append(at)

    def __traverseVertices(self):
        visited = [False for i in range(self.__verticesCount)]
        verticesStack = []

        for vertex in range(self.__verticesCount):
            self.__traverseDfs(visited, vertex, verticesStack)

        return verticesStack

    def __findComponentsDfs(self, visited, at, currentComponent):
        if visited[at]:
            return

        visited[at] = True
        currentComponent.append(at)

        for toVertex in self.__edges[at]:
            self.__findComponentsDfs(visited, toVertex, currentComponent)

    def __findComponents(self, verticesStack):
        visited = [False for i in range(self.__verticesCount)]
        result = GraphAnalysis(0, 0)

        while len(verticesStack) > 0:
            vertext = verticesStack.pop()
            if not visited[vertext]:
                component = []
                self.__findComponentsDfs(visited, vertext, component)

                verticesCount = len(component)
                if verticesCount % 2 == 1:
                    result.oddCompoonents += verticesCount
                else:
                    result.evenComponents += verticesCount

        return result

    def analyseGraph(self):
        verticesStack = self.__traverseVertices()

        self.__reverseEdges()
        return self.__findComponents(verticesStack)

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

verticesCount, edgesCount = readIntArray()
graph = Graph(verticesCount)

for i in range(edgesCount):
    fromVertex, toVertex = readIntArray()
    graph.addEdge(fromVertex-1, toVertex-1)

analysis = graph.analyseGraph()
print(analysis.oddCompoonents - analysis.evenComponents)