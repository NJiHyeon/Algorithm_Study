# 규칙에 따라 문자에 대응하는 수를 출력하는 문제(틀림)

alphabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0 
word = input()

for unit in alphabet_list :
    for i in unit : 
        for j in word : 
            if i == j :
                time += alphabet_list.index(unit) + 3

print(time)