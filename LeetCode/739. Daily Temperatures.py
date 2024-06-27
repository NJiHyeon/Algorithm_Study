'''1st : Time Limit Exceeded'''
class Solution:
    def dailyTemperatures(self, temperatures):
        answer = []
        for i in range(len(temperatures)-1):
            j = 0
            find = False
            # i=6
            while i+j+1 < len(temperatures):
                if temperatures[i] < temperatures[i+j+1]:
                    j += 1
                    find = True
                    break
                else:
                    j += 1
            if find == True:
                answer.append(j)
            else:
                answer.append(0)
        answer.append(0)
        return answer
    

'''2nd : Time Limit Exceeded'''
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures):
        temperatures = deque(temperatures)
        result = []
        while len(temperatures) > 1:
            find = True
            i = 1
            while i < len(temperatures) and temperatures[0] >= temperatures[i]:
                i += 1
                if i >= len(temperatures):
                    find = False
            if find == True:
                result.append(i)
            else:
                result.append(0)
            temperatures.popleft()
            print(temperatures)
        result.append(0)
        return result

#=============================================================================
'''Teacher code'''
def dailyTemperatures