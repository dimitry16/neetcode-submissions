class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i, num in enumerate(nums):
            numsDict[num] = i

        for j in range(len(nums)):
            if (target - nums[j]) in numsDict and (j != numsDict[target - nums[j]]):
                return [j, numsDict[target - nums[j]]]

        return []

            



        