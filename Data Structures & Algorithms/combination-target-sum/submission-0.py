class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        path = []

        def backtrack(index, path, target):
            if target == 0:
                results.append(path.copy())
                return
            if target <  0:
                return
            if index >= len(nums):
                return

            path.append(nums[index])
            backtrack(index, path, target - nums[index])
            path.pop()

            backtrack(index + 1, path, target)

        backtrack(0, path, target)
        return results