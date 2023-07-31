# 내가 푼 방법
case = int(input())
n = 0
sum = 0
for i in range(case) :
    score = list(map(int, input().split()))
    for r in range(1, score[0]+1) :
        sum = sum + score[r] 
    average = sum/score[0]
    for j in range(1, score[0]+)1 :
        if score[j] > average :
            n = n+1
    t = n/score[0]*100
    print("{:.3f}".format(t) + '%' )
    n = 0
    sum = 0


# 다른 방법
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')