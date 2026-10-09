class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        res = 0
        for i in range(k):
            res = - heapq.heappop(minHeap)
        
        return res