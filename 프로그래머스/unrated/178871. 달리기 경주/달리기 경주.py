def solution(players, callings) :
    play = {name:index for index, name in enumerate(players)}
    for cal in callings :
        i = play[cal] #현재등수
        players[i-1], players[i] = players[i], players[i-1]#등수에 따라 사람 바꾸기
        #현재등수 바꾸기
        play[players[i-1]] = i-1
        play[players[i]] = i
        
    return players

    
