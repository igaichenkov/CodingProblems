def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

n, m = readIntArray()

edges = {}
for i in range(m):
    a, b = readIntArray()
    if a not in edges:
        edges[a] = list()

    edges[a].append(b)

q = readInt()
for i in range(q):
    a, b = readIntArray()
    if a in edges and b in edges[a]:
        print("YES")
    else:
        print("NO")