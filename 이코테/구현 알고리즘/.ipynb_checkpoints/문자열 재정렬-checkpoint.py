'''My code'''
s = input()
n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
n_index = []
s_index = []
for i in range(len(s)) :
    if s[i] in n :
        n_index.append(s[i])
    else :
        s_index.append(s[i])
        
s_index.sort()
for i in s_index :
    print(i, end='')

final_n = 0
for i in n_index :
    final_n += int(i) 
print(final_n, end='')


'''Lecture code'''
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data :
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha() :
        result.append(x)
    # 숫자는 따로 더하기
    else :
        value += int(x)
        
# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0 :
    result.append(str(value))
    
# 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print(''.join(result))