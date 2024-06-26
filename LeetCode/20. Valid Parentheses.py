'''Try1'''
class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        brackets = {')' : '(',
                    ']' : '[',
                    '}' : '{'}

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                result.append(s[i])
            else:
                if len(result)>0 and result[-1]==brackets[s[i]]:
                    result.pop()
                else:
                    return False

        if len(result)==0:
            return True
        else:
            return False
    
    
solution = Solution()
solution.isValid('(([])}')
solution.isValid('(')

#=============================================================================
'''Teacher code'''
def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack