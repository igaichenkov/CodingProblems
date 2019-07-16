class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        if n == 2:
            return 2

        steps1 = 1
        steps2 = 2

        for _ in range(2, n):
            steps1, steps2 = steps2, steps1 + steps2

        return steps2
