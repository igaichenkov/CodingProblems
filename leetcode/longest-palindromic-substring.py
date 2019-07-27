import typing

class Solution:
    def longestPalindrome(self, s: str) -> str:
        padStr = self.__padString(s)

        center = 1
        right = 1
        palindromeLen = [0 for i in range(len(padStr))]

        maxPalindromeCenter = 0
        maxPalindromeLen = 0

        for i in range(1, len(padStr) - 1):
            mirror = 2 * center - i

            if i < right:
                palindromeLen[i] = min(palindromeLen[mirror], right - i)

            while (i + palindromeLen[i] + 1 < len(padStr) and 
                    i - palindromeLen[i] - 1 >= 0 and
                    padStr[i + palindromeLen[i] + 1] == padStr[i - palindromeLen[i] - 1]):
                palindromeLen[i] += 1

            if i + palindromeLen[i] > right:
                center = i
                right = i + palindromeLen[i]

            if palindromeLen[i] > maxPalindromeLen:
                maxPalindromeLen = palindromeLen[i]
                maxPalindromeCenter = i

        originalStrStartIndex = int((maxPalindromeCenter - maxPalindromeLen) / 2)
        return s[originalStrStartIndex:(originalStrStartIndex + maxPalindromeLen)]

    def __padString(self, s: str) -> str:
        stringPad = chr(0)
        for i in range(len(s)):
            stringPad += s[i] + chr(0)

        return stringPad

sol = Solution()

print(sol.longestPalindrome('babad'))