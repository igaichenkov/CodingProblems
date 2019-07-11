import copy
from queue import Queue

MAX_COST = 200 # max cost by problem definition

def readIntArray():
    return list(map(lambda x: int(x), input().split()))

def readInt():
    return int(input())

class Assignments:
    def reset(self):
        self.assignedJobs = [[False for col in range(self.__jobsNumber)] for row in range(self.__jobsNumber)]
        self.assignedRows = [False for i in range(self.__jobsNumber)]
        self.assignedCols = [False for i in range(self.__jobsNumber)]
        return self

    def __init__(self, jobsNumber):
        self.__jobsNumber = jobsNumber
        self.reset()

class Graph:
    def __init__(self, jobsNumber, costs):
        self.jobsNumber = jobsNumber
        self.__costsMatrix = costs

    def __doRowReduction(self, jobsNumber, costsMatrix):
        for row in range(jobsNumber):
            minCost = MAX_COST
            for cost in costsMatrix[row]:
                minCost = min(minCost, cost)

            for col in range(jobsNumber):
                costsMatrix[row][col] -= minCost

    def __doColReduction(self, jobsNumber, costsMatrix):
        for col in range(jobsNumber):
            minCost = MAX_COST
            for row in range(jobsNumber):
                minCost = min(minCost, costsMatrix[row][col])

            for row in range(jobsNumber):
                costsMatrix[row][col] -= minCost

    def __tryFindSolutionRecursive(self, costs, zeros, assignments: Assignments, markedCount: int, offset: int):
        if markedCount == self.jobsNumber:
            return True

        for i in range(offset, len(zeros)):
            row = zeros[i][0]
            col = zeros[i][1]

            if not assignments.assignedRows[row] and not assignments.assignedCols[col]:
                assignments.assignedRows[row] = True
                assignments.assignedCols[col] = True
                assignments.assignedJobs[row][col] = True

                if self.__tryFindSolutionRecursive(costs, zeros, assignments, markedCount+1, i+1):
                    return True

                assignments.assignedRows[row] = False
                assignments.assignedCols[col] = False
                assignments.assignedJobs[row][col] = False

        return False

    def __tryFindSolution(self, costs, assignments: Assignments):
        zeros = []
        columns = set()

        for row in range(self.jobsNumber):
            for col in range(self.jobsNumber):
                if costs[row][col] == 0:
                    zeros.append( (row, col) )
                    columns.add(col)

        if len(columns) < self.jobsNumber:
            return False

        return self.__tryFindSolutionRecursive(costs, zeros, assignments, 0, 0)

    def __findMinUncrossedCost(self, markedRows, markedCols, costs) -> int:
        minCost = MAX_COST

        for row in range(self.jobsNumber):
            for col in range(self.jobsNumber):
                if markedRows[row] and not markedCols[col] and minCost > costs[row][col]:
                    minCost = costs[row][col]

        return minCost

    def __adjustUncrossedCosts(self, markedRows, markedCols, costs):
        minCost = self.__findMinUncrossedCost(markedRows, markedCols, costs)
        for row in range(self.jobsNumber):
            for col in range(self.jobsNumber):
                if markedRows[row] and not markedCols[col]:
                    costs[row][col] -= minCost
                elif not markedRows[row] and markedCols[col]:
                    costs[row][col] += minCost

    def __assignPossibleJobs(self, costs, assignments: Assignments):
        for row in range(self.jobsNumber):
            for col in range(self.jobsNumber):
                if costs[row][col] == 0 and not assignments.assignedCols[col]:
                    assignments.assignedCols[col] = True
                    assignments.assignedRows[row] = True
                    assignments.assignedJobs[row][col] = True
                    break

    def __getJobAssignments(self, costs):
        assignments = Assignments(self.jobsNumber)

        while not self.__tryFindSolution(costs, assignments.reset()):
            self.__assignPossibleJobs(costs, assignments.reset())
            markedRows = [False for i in range(self.jobsNumber)]
            markedCols = [False for i in range(self.jobsNumber)]

            q = Queue()

            for row in range(self.jobsNumber):
                if assignments.assignedRows[row]:
                    continue

                q.put(row)
            
            while not q.empty():
                row = q.get()

                if markedRows[row]:
                    continue

                markedRows[row] = True

                for col in range(self.jobsNumber):
                    if costs[row][col] == 0 and not markedCols[col]:
                        markedCols[col] = True

                        for rowWithAssignment in range(self.jobsNumber):
                            if assignments.assignedJobs[rowWithAssignment][col]:
                                q.put(rowWithAssignment)

            self.__adjustUncrossedCosts(markedRows, markedCols, costs)
        
        return assignments.assignedJobs        


    def getMinCost(self) -> int:
        costs = copy.deepcopy(self.__costsMatrix)
        self.__doRowReduction(jobsNumber, costs)
        self.__doColReduction(jobsNumber, costs)
        assignedJobs = self.__getJobAssignments(costs)

        minCost = 0
        for row in range(self.jobsNumber):
            for col in range(self.jobsNumber):
                if assignedJobs[row][col]:
                    minCost += self.__costsMatrix[row][col]
                    break

        return minCost



jobsNumber = readInt()
costs = []

for i in range(jobsNumber):
    costs.append(readIntArray())

graph = Graph(jobsNumber, costs)
print(graph.getMinCost())