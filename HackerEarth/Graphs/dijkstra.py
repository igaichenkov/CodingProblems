from queue import PriorityQueue

class Distance:
    def __init__(self, to, dist):
        self.To = to
        self.Dist = dist

    def __lt__(self, other):
        return self.Dist < other.Dist

class Edge:
    def __init__(self, fromVertex, toVertex, weight):
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

def dijkstra(numberOfVerticies, edges):
    visited = [False for i in range(numberOfVerticies)]
    dist = [int(1e9) for i in range(numberOfVerticies)]
    dist[0] = 0

    queue = PriorityQueue(numberOfVerticies)
    queue.put(Distance(0, 0))

    while not queue.empty():
        vertexDist = queue.get(block = False)
        if visited[vertexDist.To]:
            continue

        visited[vertexDist.To] = True

        for edge in edges[vertexDist.To]:
            if dist[vertexDist.To] + edge.weight < dist[edge.toVertex]:
                dist[edge.toVertex] = dist[vertexDist.To] + edge.weight
                queue.put(Distance(edge.toVertex, dist[vertexDist.To] + edge.weight))

    return dist

def floydWarshall(numberOfVerticies, edges):
    for k in range(numberOfVerticies):
        for i in range(numberOfVerticies):
            for j in range(numberOfVerticies):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def bellmanFord(numberOfVerticies, edges):
    dist = [1e9 for i in range(numberOfVerticies)]
    dist[0] = 0

    for i in range(numberOfVerticies - 1):
        for j in range(numberOfVerticies):
            if dist[edges[j].fromVertex] + edges[j].weight < dist[edges[j].toVertex]:
                dist[edges[j].toVertex] = dist[edges[j].fromVertex] + edges[j].weight

    return dist


numberOfVerticies, numberOfEdges = readIntArray()
edges = []

for i in range(numberOfEdges):
    fromVertex, toVertex, weight = readIntArray()
    edges.append(Edge(fromVertex - 1, toVertex - 1, weight))

dist = bellmanFord(numberOfVerticies, edges)

print(" ".join(list(map(lambda d: str(d), dist[1:]))))