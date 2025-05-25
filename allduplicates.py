class Solution(object):
    def findDuplicates(self, nums):
        sets=set()
        empty=[]
        for i in nums:
            if i in sets:
                empty.append(i)
            else:
                sets.add(i)
        return empty