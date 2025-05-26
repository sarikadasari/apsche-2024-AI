class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for ind,val in enumerate(nums):
            d=target-val
            if d in hashmap:
                return [ind,hashmap[d]]
            hashmap[val]=ind