import queue

def readInt():
    return int(input())

def reverse(str, length):
    length += 1
    return str[:length][::-1] + str[length:]

n = readInt()
arr = input().split()
original = "".join(arr)

arr.sort()
dest = "".join(arr)

operationsCount = {}
operationsCount[original] = 0
q = queue.Queue()
q.put(original)

while not q.empty():
    val = q.get()

    if val == dest:
        print(operationsCount[val])
        break

    for i in range(1, n):
        tmp = val
        tmp = reverse(tmp, i)
        if tmp not in operationsCount:
            operationsCount[tmp] = operationsCount[val] + 1
            q.put(tmp)
