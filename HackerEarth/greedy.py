def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

def countBottles(containerCapacity, capacitiesOfBottles):
    bottlesCounter = 0

    for cap in capacitiesOfBottles:
        containerCapacity -= cap
        if containerCapacity <= 0:
            break

        bottlesCounter += 1

    return bottlesCounter

testsNumber = readInt()

for testIndex in range(testsNumber):
    numberOfBottles, containerCapacity = readIntArray()
    capacitiesOfBottles = readIntArray()

    capacitiesOfBottles.sort()
    bottlesCount = countBottles(containerCapacity, capacitiesOfBottles)

    print(bottlesCount)
