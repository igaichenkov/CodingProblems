import sys
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestSum = nums[0] + nums[1] + nums[2]
        minDiff = abs(target - closestSum)

        nums = sorted(nums)
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                diff = abs(sum - target)
                if diff < minDiff:
                    closestSum = sum
                    minDiff = diff
                    
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    break

        return closestSum
