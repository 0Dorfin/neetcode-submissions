class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        racha = 0
        numeros_set = set(nums)

        for num in nums:
            if num - 1 not in numeros_set:
                racha_actual = 1
                siguiente = num + 1
                while siguiente in numeros_set:
                    racha_actual += 1
                    siguiente += 1

                if racha_actual > racha:
                    racha = racha_actual

        return racha