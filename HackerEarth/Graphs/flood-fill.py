class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, another):
        return self.row == another.row and self.col == another.col

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

def checkAdjCell(field, currentPosition, step, stack):
    nextRow = currentPosition.row + step[0]
    nextCol = currentPosition.col + step[1]

    if (nextRow < 0 or nextRow >= len(field) or nextCol < 0 or nextCol >= len(field[0])
            or field[nextRow][nextCol] == 0):
        return

    stack.append(Position(nextRow, nextCol))

def isReachable(destRow, destCol, field):
    stack = [Position(0, 0)]
    dest = Position(destRow, destCol)

    visited = [[False for i in range(rows)] for j in range(cols)]

    while len(stack) > 0:
        currentPosition = stack.pop()
        if currentPosition == dest:
            return True

        if visited[currentPosition.row][currentPosition.col]:
            continue

        visited[currentPosition.row][currentPosition.col] = True

        checkAdjCell(field, currentPosition, (-1, 0), stack)
        checkAdjCell(field, currentPosition, (1, 0), stack)
        checkAdjCell(field, currentPosition, (0, -1), stack)
        checkAdjCell(field, currentPosition, (0, 1), stack)

    return False

rows, cols = readIntArray()
field = []

for i in range(rows):
    field.append(readIntArray())

isReachable = isReachable(rows-1, cols-1, field)
if isReachable:
    print("Yes")
else:
    print("No")