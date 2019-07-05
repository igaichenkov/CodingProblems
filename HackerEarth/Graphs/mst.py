class Edge:
    def __init__(self, fromVertex, toVertex, weight):
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.weight = weight

class Graph:
    def __init__(self, numVerticies):
        self.__id = []
        for i in range(numVerticies):
            self.__id.append(i)

        self.__edges = []

    def __root(self, node):
        while self.__id[node] != node:
            self.__id[node] = self.__id[self.__id[node]]
            node = self.__id[node]

        return node

    def __union(self, node1, node2):
        node1Root = self.__root(node1)
        node2Root = self.__root(node2)

        self.__id[node1Root] = node2Root

    def addEdge(self, fromVertex, toVertex, weight):
        self.__edges.append(Edge(fromVertex, toVertex, weight))

    def getMinTreeWeight(self):
        sumCost = 0

        for edge in sorted(self.__edges, key=lambda edge: edge.weight, reverse=False):
            root1 = self.__root(edge.fromVertex)
            root2 = self.__root(edge.toVertex)

            if root1 != root2:
                self.__union(root1, root2)
                sumCost += edge.weight

        return sumCost

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

numVerticies, numEdges = readIntArray()
graph = Graph(numVerticies)

for i in range(numEdges):
    fromVertex, toVertex, weight = readIntArray()
    graph.addEdge(fromVertex - 1, toVertex - 1, weight)

print(graph.getMinTreeWeight())