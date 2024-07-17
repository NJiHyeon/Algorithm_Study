"""
입력받은 단어 중에서 어떤 알파벳의 빈도가 가장 높은지 확인하여 그 알파벳을 출력
"""
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성
# 단, 대문자와 소문자를 구분하지 않는다.
words = input().upper()
unique_words = list(set(words))
cnt_list = []

for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print("?")
    
else :
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])
    
    
    




