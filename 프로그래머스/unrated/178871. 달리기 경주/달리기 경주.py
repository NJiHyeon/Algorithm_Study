# 해결방법
'''
1. calling에서 순서대로 이름들을 호출하고,
이름이 호출되면 그 이름의 인덱스를 찾는다. 
2. 해당 인덱스랑 현재-1번째 인덱스랑 위치 바꾸기 (players)
(시간초과 해결) 리스트 -> 딕셔너리
'''
#players = ["mumu", "soe", "poe", "kai", "mine"]
#callings = ["kai", "kai", "mine", "mine"]
#result = ["mumu", "kai", "mine", "soe", "poe"] # 출력돼야함
def solution(players, callings) :
    players_rank = [i for i in range(1, len(players)+1)]
    dic = dict(zip(players, players_rank))
    dic_rev = dict(map(reversed, dic.items()))
    for i in range(0, len(callings)) :
        win_name = callings[i] # kai
        win_rank = dic[win_name] # 4
        lose_rank = win_rank - 1  # 3
        lose_name = dic_rev[lose_rank] # poe
        
        dic[win_name] = lose_rank
        dic[lose_name] = win_rank
        dic_rev[lose_rank] = win_name
        dic_rev[win_rank] = lose_name
        
    d = sorted(dic_rev.items())
    dd = []
    for i in range(len(d)) :
        dd.append(d[i][1])
    
    return dd


    