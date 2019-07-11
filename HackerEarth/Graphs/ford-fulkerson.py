from queue import Queue
import sys

class Graph:
    def __init__(self, verticesCount):
        self.__edges = [[0 for j in range(verticesCount)] for i in range(verticesCount)]
        self.__verticesCount = verticesCount

    def addEdge(self, fromVertex, toVertex, capacity):
        self.__edges[fromVertex][toVertex] = capacity

    def __initVisistedFlags(self):
        visited = [False for i in range(self.__verticesCount)]
        visited[0] = True

        return visited

    def getMaxFlow(self, source, sink):
        visited = self.__initVisistedFlags()

        parent = [-1 for i in range(self.__verticesCount)]
        q = Queue()
        q.put(source)
        maxFlow = 0

        while not q.empty():
            vertex = q.get_nowait()

            for to in range(self.__verticesCount):
                if self.__edges[vertex][to] != 0 and not visited[to]:
                    parent[to] = vertex
                    visited[to] = True

                    if to == sink:
                        flow = self.__findMinFlow(parent, source, sink)
                        maxFlow += flow
                        self.__updateResidualFlow(parent, source, sink, flow)
                        visited = self.__initVisistedFlags()
                        q = Queue()
                        q.put_nowait(source)

                        break

                    q.put(to)

        return maxFlow

    def __getFlow(self, parentMapping, source, sink):
        minFlow = self.__findMinFlow(parentMapping, source, sink)
        current = sink

        while current != source:
            parent = parentMapping[current]

            self.__edges[parent][current] -= minFlow
            self.__edges[current][parent] += minFlow
            
            current = parent

    def __updateResidualFlow(self, parentMapping, source, sink, minFlow):
        current = sink

        while current != source:
            parent = parentMapping[current]

            self.__edges[parent][current] -= minFlow
            self.__edges[current][parent] += minFlow

            current = parent

    def __findMinFlow(self, parentMapping, source, sink):
        current = sink
        parent = parentMapping[current]
        minFlow = self.__edges[parent][current]
        current = parent

        while current != source:
            parent = parentMapping[current]
            currentFlow = self.__edges[parent][current]
            if minFlow > currentFlow:
                minFlow = currentFlow

            current = parent

        return minFlow

        

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

verticesCount, edgesCount = readIntArray()
graph = Graph(verticesCount)

for i in range(edgesCount):
    fromVertex, toVertex, capacity = readIntArray()
    graph.addEdge(fromVertex, toVertex, capacity)

source, sink = readIntArray()
print(graph.getMaxFlow(source, sink))
