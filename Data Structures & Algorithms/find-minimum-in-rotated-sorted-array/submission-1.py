class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[m] and nums[m] < nums[r]:
                return nums[l] 
            elif nums[r] < nums[l] and nums[l] < nums[m]:
                l = m + 1
            elif nums[m] < nums[r] and nums[r] < nums[l]:
                r = m
            if l == r or l==m:
                return min(nums[l],nums[r]) 
        