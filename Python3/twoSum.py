class Solution:
    def twoSum(self, nums, target):
        
        comp = dict()
        # nums = [2,7,11,15] target = 7
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            
            if num in cmap:
                return [cmap[num], i]
            else:
                comp[diff] = i
