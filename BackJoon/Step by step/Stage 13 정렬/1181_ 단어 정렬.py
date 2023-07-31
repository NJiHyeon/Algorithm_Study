# 단어의 순서를 정의하여 정렬하는 문제
#--------------------------------------------------------------------------------------------
# My Code -> 시간초과
import sys
N = int(sys.stdin.readline())
word_list = []
for i in range(N) :
    word_list.append(sys.stdin.readline())

# 고려 : 단어의 길이, 알파벳 순서, 중복 단어는 한번만 출력
# 1) 알파벳 순서
word_list.sort()

# 2) 단어의 길이
for i in range(N) :
    for j in range(N - i - 1) :
        if len(word_list[j]) > len(word_list[j+1]) :
            word_list[j], word_list[j+1] = word_list[j+1], word_list[j]


# 3) 중복 단어 제거
for i in range(len(word_list)-1) :
    if word_list[i] == word_list[i+1] :
        del word_list[i]
      
for i in word_list :
    print(i)


#--------------------------------------------------------------------------------------------
# 다시 -> 시간초과 ..
import sys
N = int(sys.stdin.readline())
word_list = []
for i in range(N) :
    word_list.append(input())

# 💡 중복 단어 제거를 코드 구현으로 안하고 set을 쓰면 바로 됨 ...
word_list = list(set(word_list))
word_list.sort()
word_list

for i in range(len(word_list)) :
    for j in range(len(word_list) - i - 1) :
        if len(word_list[j]) > len(word_list[j+1]) :
            word_list[j], word_list[j+1] = word_list[j+1], word_list[j]


for i in word_list :
    print(i)

#--------------------------------------------------------------------------------------------
# Googling Code + MY ⭕
import sys
N = int(sys.stdin.readline())
word_list = []
for i in range(N) :
    word_list.append(input())

# 중복 처리 : 중복 단어 제거를 코드 구현으로 안하고 set을 쓰면 바로 됨 ...
word_list = list(set(word_list))

# 길이 표현
new = []
for i in word_list :
    new.append((len(i), i))

# 길이 및 사전 순서 처리
new.sort()

# 출력
for l, w in new :
    print(w)