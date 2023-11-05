def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    new = []
    for b in babbling : 
        b = b.replace("aya", '1')
        b = b.replace("ye", '2')
        b = b.replace("woo", '3')
        b = b.replace("ma", '4')
        new.append(b)
    
    for bb in new :
        if bb.isdigit() :
            if '22' not in bb and '11' not in bb and '33' not in bb and '44' not in bb :
                answer += 1
            
    return answer