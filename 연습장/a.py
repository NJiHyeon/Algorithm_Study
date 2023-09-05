name = ["may", "kein", "kain", "radi"]
yearing = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],
         ["may", "kein", "brin", "deny"], 
         ["kon", "kain", "may", "coni"]]

result = []
for group in photo : 
    score = 0
    for person in group :
        if person in name :
            i = name.index(person)
            score += yearing[i]
    result.append(score)
result
for i in photo :
    #print(i)
    for person in i :
        print(person)
        
name.index("may")
result += yearing[0]

yearing[0]

s = "banana"
s = "foobar"
# 내풀이
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)) :
        if s[i] not in dic :
            answer.append(-1)
        else :
            answer.append(i-dic[s[i]])
        dic[s[i]] = i
    return answer


def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer

def solution(n, m, section):
    answer = 1 # 칠하는 횟수
    paint = section[0] # 덧칠 시작점
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
            
    return answer



def solution(n):
    n_list = []
    for i in range(len(str(n))) :
        n_list.append(n[i])
    answer = n_list[::-1]
    return answer

n = '123'
from math import sqrt
n = 133
answer = -1
point = int(sqrt(n))
for i in range(1, point+1) :
    if i*i == n :
        answer = (i+1)*(i+1)

s = "1 2 3 4"
s_list = list(map(int, s.split()))
s_list