def solution(numbers, hand):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 0, 22]]
    l = [1, 4, 7]
    r = [3, 6, 9]
    answer = ''
    hand_l = [3, 0]
    hand_r = [3, 2]
    hand_h = [0, 0]
    
    for n in numbers :
        if n in l :
            answer += "L"
            for i in range(4) :
                for j in range(3) :
                    if keypad[i][j]==n :
                        hand_l[0]=i
                        hand_l[1]=j
                        
        elif n in r :
            answer += "R"
            for i in range(4) :
                for j in range(3) :
                    if keypad[i][j]==n :
                        hand_r[0]=i
                        hand_r[1]=j
                        
        else :
            for i in range(4) :
                for j in range(3) :
                    if keypad[i][j]==n :
                        hand_h[0]=i
                        hand_h[1]=j
            d_l = abs(hand_h[0]-hand_l[0]) + abs(hand_h[1]-hand_l[1])
            d_r = abs(hand_h[0]-hand_r[0]) + abs(hand_h[1]-hand_r[1])
            if d_l == d_r :
                if hand == 'right' :
                    answer += "R"
                    hand_r[0] = hand_h[0]
                    hand_r[1] = hand_h[1]
                else :
                    answer += "L"
                    hand_l[0] = hand_h[0]
                    hand_l[1] = hand_h[1]
                
            else :
                if d_l < d_r :
                    answer += "L"
                    hand_l[0] = hand_h[0]
                    hand_l[1] = hand_h[1]
                else :
                    answer += "R"
                    hand_r[0] = hand_h[0]
                    hand_r[1] = hand_h[1]
            
    return answer