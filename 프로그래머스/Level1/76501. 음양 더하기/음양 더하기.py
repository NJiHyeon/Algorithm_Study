def solution(absolutes, signs):
    for i in range(len(absolutes)) :
        if signs[i] == False :
            absolutes[i] = -absolutes[i]
    return sum(absolutes)

'''
# 좋은코드
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
'''