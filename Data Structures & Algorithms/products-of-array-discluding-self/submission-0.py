class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left_product = [1] * l
        right_product = [1] * l
        for i in range(1, l):
            left_product[i] = left_product[i-1] * nums[i-1]

        for i in range(l-2,-1,-1):
            right_product[i] = right_product[i+1] * nums[i+1]

        result = [left_product[i] * right_product[i] for i in range(l)]
        return result
