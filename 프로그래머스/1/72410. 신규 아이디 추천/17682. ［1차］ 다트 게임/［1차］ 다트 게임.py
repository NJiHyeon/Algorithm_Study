def solution(dartResult):
    answer = []
    game = 0
    dartResult = dartResult.replace('10', 't')
    bonus = ['', 'S', 'D', 'T']
    option = ['*', '#']
    for d in dartResult :
        # 1S*2T*3S
        if d.isdigit() :
            answer.append(game)
            game = int(d)
        elif d=='t' :
            answer.append(game)
            game = 10
        else :
            if d in bonus :
                game = game**(bonus.index(d))
            elif d in option :
                if len(answer)==0:
                    if d=='*' :
                        game *= 2
                    else :
                        game *= (-1)
                else :
                    if d=='*' :
                        game *= 2
                        answer[-1] *= 2
                    else :
                        game *= (-1)
    return sum(answer)+game
                    
                
        
        