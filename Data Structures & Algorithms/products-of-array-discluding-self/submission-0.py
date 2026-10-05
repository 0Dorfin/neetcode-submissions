class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acumulador = []
        pre = 1

        for num in nums:
            acumulador.append(pre)
            pre = pre * num
        
        post = 1
        for num in range(len(nums) -1, -1, -1):
            acumulador[num] = acumulador[num] * post
            post = post * nums[num]

        return acumulador