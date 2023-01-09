# 크로아티아 알파벳의 개수를 세는 문제

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')
    
print(len(word))