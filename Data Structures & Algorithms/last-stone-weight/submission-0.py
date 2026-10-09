class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone_one = heapq.heappop(stones)
            stone_two = heapq.heappop(stones)

            if stone_one > stone_two:
                diff = stone_one - stone_two
                heapq.heappush(stones, diff)
            else:
                diff = stone_one - stone_two
                heapq.heappush(stones, diff)
        
        return abs(stones[0])

