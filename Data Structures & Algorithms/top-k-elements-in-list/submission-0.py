class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        sorted_frequency = list(sorted(frequency, key=frequency.get, reverse=True))

        return sorted_frequency[:k]