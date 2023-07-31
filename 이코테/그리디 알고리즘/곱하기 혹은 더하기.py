### My code
s = input()

array = []
for i in s :
    array.append(int(i))
    
while True :
    if len(array) == 1 :
        break
    else :
        if array[0] == 0 or array[0] == 1 or array[1] == 0 or array[1] == 1 :
            array[0] = array[0]+array[1]
            del array[1]
        else :
            array[0] = array[0] * array[1]
            del array[1]
            
print(array[0])


### Lecture code
data = input()

# 첫번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)) :
    # 두 수 중에서 하나라도 '0', '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += num
    else :
        result *= num
        
print(result)