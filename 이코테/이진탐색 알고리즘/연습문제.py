# 떡볶이 떡 만들기
'''My Code'''
'''6cm 이상되도록하는 M의 최댓값 ! => output : 15''''
N, M = map(int, input().split())
n_list = list(map(int, input().split()))

from bisect import bisect_right, bisect_left
n_list.sort() # [10, 15, 17, 19] -> [-1]번 인덱스부터 하나씩 줄이도록, 
h = n_list[-1]-1

def cutting(n_list, h) :
    while True :
        cut_right_index = bisect_right(n_list, h)
        new_list = n_list[cut_right_index :]
        output = sum(list(map(lambda x:x -h, new_list)))
        #print(new_list, output)
        
        if output >= M :
            return h
        else :
            return cutting(n_list, h-1)
        
print(cutting(n_list, h)
      

'''Solution Code'''
