def solution(word):
    from itertools import product
    alphabet = ['A', 'E', 'I', 'O', 'U']
    word_list = []
    word_dict = {}
    
    for i in range(1, 6) :
        word_list += list(product(alphabet, repeat=i))
    word_list.sort()
    
    for i in range(len(word_list)) :
        word_dict[''.join(word_list[i])] = i+1
    return word_dict[word]
        