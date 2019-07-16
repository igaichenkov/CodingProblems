from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = dict()
        for i in range(len(nums)):
            dictionary[nums[i]] = i

        for i in range(len(nums)):
            secondValue = target - nums[i]

            if secondValue in dictionary:
                secondIndex = dictionary[secondValue]
                if secondIndex != i:
                    return [i, dictionary[secondValue]]