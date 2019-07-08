class GraphAnalysis:
    def __init__(self, bridges, articulationPoints):
        self.bridges = bridges
        self.articulationPoints = articulationPoints

class Graph:
    def __init__(self, verticesCount):
        self.__edges = [[] for i in range(verticesCount)]
        self.__verticesCount = verticesCount
        self.__time = 0

    def addEdge(self, fromVertex, toVertex):
        self.__edges[fromVertex].append(toVertex)
        self.__edges[toVertex].append(fromVertex)

    def __dfs(self, visited, discoveryTime, lowLink, parent, at, bridges, articulationPoints):
        visited[at] = True
        self.__time += 1
        discoveryTime[at] = lowLink[at] = self.__time

        childrenCount = 0

        for to in self.__edges[at]:
            if to == parent:
                continue

            if not visited[to]:
                childrenCount += 1

                self.__dfs(visited, discoveryTime, lowLink, at, to, bridges, articulationPoints)
                lowLink[at] = min(lowLink[at], lowLink[to])
                if discoveryTime[at] < lowLink[to]:
                    bridge = (at, to)
                    bridges.append(bridge)

                if parent != -1 and discoveryTime[at] <= lowLink[to]:
                    articulationPoints.append(at)
            else:
                lowLink[at] = min(discoveryTime[to], lowLink[at])

        if childrenCount > 1 and parent == -1:
            articulationPoints.append(at)

    def analyseGraph(self):
        visited = [False for i in range(verticesCount)]
        discoveryTime = [0 for i in range(verticesCount)]
        lowLink = [0 for i in range(verticesCount)]
        bridges = []
        articulationPoints = []

        self.__time = 0
        
        for vertex in range(verticesCount):
            if visited[vertex]:
                continue

            self.__dfs(visited, discoveryTime, lowLink, -1, vertex, bridges, articulationPoints)

        return GraphAnalysis(bridges, articulationPoints)

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

print(len(analysis.articulationPoints))
for vertext in reversed(analysis.articulationPoints):
    print(vertext, end=' ')

print('')

print(len(analysis.bridges))

for bridge in reversed(analysis.bridges):
    print(bridge[0], bridge[1], sep=' ')