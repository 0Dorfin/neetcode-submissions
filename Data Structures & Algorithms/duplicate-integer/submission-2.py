class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        
        numbers_viewed = set()

        for num in nums:
            if num in numbers_viewed:
                return True
            else:
                numbers_viewed.add(num)
        return False
