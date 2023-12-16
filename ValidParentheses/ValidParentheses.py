class Solution(object):
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        # solution with map
        lastOpen = ''
        m = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        c = 0

        for i in s:
            c +=1
            if i in ['(','[','{']:
                lastOpen = i
            elif i in m and m[i] != lastOpen:
                print('ko')
                return
            elif c == len(s):
                print('ok')
            
        # longer solution
                
        # openRound = 0
        # openSquare = 0
        # openBraket = 0
        # lastOpen = ''       
        # for i in s:
        #     if i == '(':
        #         openRound += 1
        #         lastOpen = i
        #     elif i == '[':
        #         openSquare += 1
        #         lastOpen = i
        #     elif i == '{':
        #         openBraket += 1
        #         lastOpen = i
        #     elif i == ')' and lastOpen == '(':
        #         openRound -=1
        #     elif i == ']' and lastOpen == '[':
        #         openSquare -=1
        #     elif i == '}' and lastOpen == '{':
        #         openBraket -=1
        #     else:
        #         print('error')
        #         break
        # if openRound == 0 and openSquare == 0 and openBraket == 0:
        #     print('ok')

    isValid("()")
    isValid("()[]{}")
    isValid("(]")