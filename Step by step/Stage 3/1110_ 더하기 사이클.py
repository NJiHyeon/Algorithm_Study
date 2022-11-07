# 방법1
n = int(input())
num = n
cnt = 0

while True :
    a = num//10
    b = num%10
    c = (a+b)%10
    num = (b*10)+c
    
    cnt = cnt+1
    if (num==n) :
        break
print(cnt)

# 방법2
n = input()
num = n
cnt = 0
while 1 :
    if len(num) == 1 :
        num = "0"+num
    plus = str(int(num[0])+ int(num[1]))
    num = num[-1] + plus[-1]
    cnt += 1
    if num == n :
        print(cnt)
        break