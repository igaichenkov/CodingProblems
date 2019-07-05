from functools import reduce

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

n, m = readIntArray()
edges = [[] for i in range(n)]
visited = [False for i in range(n)]
stack = []

for i in range(m):
    nodeA, nodeB = readIntArray()
    nodeA -= 1
    nodeB -= 1
    edges[nodeA].append(nodeB)
    edges[nodeB].append(nodeA)

headNode = readInt() - 1
stack.append(headNode)
visited[headNode] = True

while len(stack) > 0:
    node = stack.pop()

    for edge in edges[node]:
        if not visited[edge]:
            visited[edge] = True
            stack.append(edge)

unreachableCount = reduce((lambda count, item: count + (0 if item else 1)), visited, 0)

print(unreachableCount)