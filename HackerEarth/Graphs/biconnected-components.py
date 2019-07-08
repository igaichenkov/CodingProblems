def last(arr):
    return arr[len(arr) - 1]

class GraphAnalysis:
    def __init__(self, oddCompoonents, evenComponents):
        self.oddCompoonents = oddCompoonents
        self.evenComponents = evenComponents

class Graph:
    def __init__(self, verticesCount):
        self.__edges = [[] for i in range(verticesCount)]
        self.__verticesCount = verticesCount
        self.__time = 0

    def addEdge(self, fromVertext, toVertex):
        self.__edges[fromVertex].append(toVertex)
        self.__edges[toVertex].append(fromVertex)

    def __dfs(self, visited, discoveryTime, lowLink, parent, at, currentComponent, analysis: GraphAnalysis):
        visited[at] = True
        discoveryTime[at] = lowLink[at] = self.__time
        self.__time += 1

        currentComponent.append(at)

        childrenCount = 0

        for to in self.__edges[at]:
            if to == parent:
                continue

            if not visited[to]:
                childrenCount += 1

                self.__dfs(visited, discoveryTime, lowLink, at, to, currentComponent, analysis)
                lowLink[at] = min(lowLink[at], lowLink[to])

                if parent != -1 and discoveryTime[at] <= lowLink[to]:
                    self.__onArticulationPointFound(at, currentComponent, analysis)
            else:
                lowLink[at] = min(discoveryTime[to], lowLink[at])

        if childrenCount > 1 and parent == -1:
            self.__onArticulationPointFound(at, currentComponent, analysis)

    def __onArticulationPointFound(self, at, componentVertices, analysis: GraphAnalysis):
        itemsCount = 1
        while last(componentVertices) != at:
            itemsCount += 1
            componentVertices.pop()

        if itemsCount % 2 == 1:
            analysis.oddCompoonents += 1
        else:
            analysis.evenComponents += 1

    def analyseGraph(self):
        visited = [False for i in range(verticesCount)]
        discoveryTime = [0 for i in range(verticesCount)]
        lowLink = [0 for i in range(verticesCount)]

        self.__time = 0
        result = GraphAnalysis(0, 0)

        for vertex in range(verticesCount):
            if visited[vertex]:
                continue

            currentComponent = []
            self.__dfs(visited, discoveryTime, lowLink, -1, vertex, currentComponent, result)
            if len(currentComponent) > 0:
                self.__onArticulationPointFound(vertex, currentComponent, result)

        return result

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

verticesCount, edgesCount = readIntArray()
graph = Graph(verticesCount)

for i in range(edgesCount):
    fromVertex, toVertex = readIntArray()
    graph.addEdge(fromVertex, toVertex)

analysis = graph.analyseGraph()
print(analysis.oddCompoonents, analysis.evenComponents)