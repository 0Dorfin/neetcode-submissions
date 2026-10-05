class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, n in enumerate(nums):
            j = target - n
            if j in numMap:
                return [numMap[j], i]
            numMap[n] = i
        return