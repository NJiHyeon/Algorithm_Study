def solution(babbling):
    answer = 0
    for baby in babbling :
        if talk(baby) == True :
            answer += 1
    return answer

def talk(baby) : # ayaye
    t = [ "aya", "ye", "woo", "ma"]
    for tt in t :
        if tt in baby :
            baby = baby.replace(tt, '.')
    baby = baby.replace('.', '')
    if baby == '' :
        return True
    else :
        return False
    