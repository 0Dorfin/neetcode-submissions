class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()

        for n in nums:
            if n in vistos:
                return True
            vistos.add(n)
        return False
        