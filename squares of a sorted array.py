class Solution(object):
    def sortedSquares(self, nums):
        ret=[]
        for i in nums:
            ret.append(i**2)
            ret.sort()
        return ret