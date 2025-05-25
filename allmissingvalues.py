class Solution(object):
    def findDisappearedNumbers(self, nums):
        setns=set(nums)
        ret=[]
        for i in range(1,len(nums)+1):
            if i not in setns:
                ret.append(i)
        return ret