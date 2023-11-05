def solution(players, callings) :
    '''
    player_dict = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        idx = player_dict[call]
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        player_dict[players[idx]] = idx
        player_dict[players[idx-1]] = idx-1
    '''
    #play = dict()
    #for p in players :
        #play[p] = players.index(p) #{'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
    play = {player: idx for idx, player in enumerate(players)}
    for cal in callings :
        i = play[cal] #현재등수 kai:3
        players[i-1], players[i] = players[i], players[i-1] #["mumu", "soe", "kai", poe", "mine"]
        play[players[i]] = i
        play[players[i-1]] = i-1

    
    return players


    