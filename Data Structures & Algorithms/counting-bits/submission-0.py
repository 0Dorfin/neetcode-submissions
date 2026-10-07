class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0, n + 1):
            counter = 0
            while i > 0:
                if i & 1 == 1:
                    counter += 1
                i = i >> 1
            res.append(counter)
        
        return res