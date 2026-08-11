class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        start_nums = [num for num in num_set if num-1 not in num_set]

        current_best = 0
        for start_num in start_nums:
            count = 1
            while start_num + 1 in num_set:
                count += 1 
                start_num +=1
            current_best = max(current_best, count)

        return current_best        