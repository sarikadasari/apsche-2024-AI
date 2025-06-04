class Solution(object):
    def minimumAbsDifference(self, arr):
      arr.sort()
      min_diff=float('inf')
      for i in range(1,len(arr)):
        min_diff=min(min_diff,arr[i]-arr[i-1])
      ret=[]
      for i in range(1,len(arr)):
        if arr[i]-arr[i-1] == min_diff:
            ret.append([arr[i-1],arr[i]])
      return ret
