def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

def repair(field, line, cell, size):
    for i in range(size):
        for j in range(size):
            field[i+line][j+cell] ^= 1

def countSteps(n, m, k, field):
    result = 0

    for line in range(n):
        for cell in range(m):
            if field[line][cell] == 0:
                if line + k > n or cell + k > m:
                    return -1
                
                repair(field, line, cell, k)
                result += 1

    return result

n, m, k = readIntArray()
field = []

for i in range(n):
    field.append(readIntArray())

stepsCount = countSteps(n, m, k, field)
print(stepsCount)