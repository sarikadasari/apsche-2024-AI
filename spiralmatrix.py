class Solution(object):
    def spiralOrder(self,matrix):
        ret=[]
        while matrix:
            ret+=matrix.pop(0)   #1
            if matrix and matrix[0]:   #2
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret+=matrix.pop()[::-1]  #3
            if matrix and matrix[0]:   #4
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret