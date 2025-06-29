class Solution(object):
    def isValid(self, s):
        inp={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char in inp:
                if not stack or stack[-1]!=inp[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack)==0