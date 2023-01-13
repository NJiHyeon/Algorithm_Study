# 크로아티아 알파벳의 개수를 세는 문제
    # 다른 개수세기 문제와는 달리 2개 이상의 알파벳이 하나의 문자로 취급된다. 

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')
    
print(len(word))
