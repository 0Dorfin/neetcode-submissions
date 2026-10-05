class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum_two = numbers[left] + numbers[right]
            if sum_two < target:
                left += 1
            elif sum_two > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []