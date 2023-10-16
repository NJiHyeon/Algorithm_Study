def solution(a, b):
    # 윤년 : 2월 29일 있음
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    bb = -1
    for i in range(1, a) :
        bb += month[i]
    bb += b # 1월 1일 부터 bb일 후
    dd = bb%7
    answer = day[dd]
    return answer