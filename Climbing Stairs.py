class Solution(object):
    def climbStairs(self, n):
        dp=[0]*(n+1)
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        a,b=1,2
        for i in range(3,n+1):
            a,b=b,a+b
        return b
            
