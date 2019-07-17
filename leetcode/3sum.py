from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1

        return triplets