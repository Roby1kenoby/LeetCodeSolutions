class Solution(object):
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        m = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for p in s:
            if p in ('(','[','{'):
                stack.append(p)
            elif p in m:
                if stack and m[p] == stack[-1]:
                    stack.pop()
                else:
                    print('ko')
                    return
        if not stack:
            print('ok')
        else:
            print('ko')
        

      

    isValid("()")
    isValid("()[{}")
    isValid("")