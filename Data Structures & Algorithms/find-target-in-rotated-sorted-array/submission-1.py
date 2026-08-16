class Solution:
    def findSplit(self, nums):
        l = 0 
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1 
            elif nums[m] < nums[l]:
                r = m
            else:
                return l
        return l

    def BinarySearch(self, nums,target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        return -1

    def search(self, nums: List[int], target: int) -> int:
        splitIDX = self.findSplit(nums)
        half1 = nums[0:splitIDX]
        half2 = nums[splitIDX:] 
        b1 = self.BinarySearch(half1,target)
        b2 = self.BinarySearch(half2,target)
        if b2 == -1:
            return max(b1, b2)
        else:
            return max(b1, splitIDX + b2)

        