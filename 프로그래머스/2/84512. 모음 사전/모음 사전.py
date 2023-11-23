def solution(word):
    answer = 0
    from itertools import product
    words = []
    for i in range(1, 6) :
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat = i) :
            words.append(''.join(c))
    words.sort()        
    return words.index(word)+1