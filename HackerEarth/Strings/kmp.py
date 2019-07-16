class KMP:
    def __buildPrefixArray(self, pattern):
        prefixes = [0 for i in range(len(pattern))]

        j = 0

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = prefixes[j - 1]

            if pattern[i] == pattern[j]:
                j += 1

            prefixes[i] = j

        return prefixes

    def find(self, string, pattern):
        prefixes = self.__buildPrefixArray(pattern)
        matchesCount = 0

        j = 0
        for i in range(len(string)):
            while j > 0 and pattern[j] != string[i]:
                j = prefixes[j - 1]

            if string[i] == pattern[j]:
                j += 1
                
                if j == len(pattern):
                    matchesCount += 1
                    j = prefixes[j - 1]
                
        return matchesCount
            
pattern = input()
string = input()

kmp = KMP()
print(kmp.find(string, pattern))