class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow = self.__pow(x, abs(n))

        if n < 0:
            pow = 1 / pow

        return pow

    def __pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n % 2 == 0:
            val = self.myPow(x, int(n / 2))
            return val * val
        else:
            return x * self.myPow(x, n - 1)


sol = Solution()
print(sol.myPow(2.0, 10))
print(sol.myPow(2.1, 3))
print(sol.myPow(2.0, -2))