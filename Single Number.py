class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        i=0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                return nums[i]
            i+=2
        return nums[-1]
        
