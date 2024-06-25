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