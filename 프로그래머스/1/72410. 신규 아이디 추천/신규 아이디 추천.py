def solution(new_id):
    # new_id : "...!@BaT#*..y.abcdefghijklm"	
    spec =['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/']
    answer = ''
    '''1단계'''
    new_id = new_id.lower()
    '''2단계'''
    for i in range(len(new_id)):
        if new_id[i] not in spec:
            answer += new_id[i]
    new_id = answer
    '''3단계'''
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    '''4단계'''
    l = len(new_id)
    if l == 0:
        pass
    elif l == 1 and new_id[0] == '.':
        new_id = ''
        l -= 1
    else:
        if new_id[0] == '.':
            new_id = new_id[1:]
            l -= 1
        if new_id[-1] == '.':
            new_id = new_id[:-1]
            l -= 1
    
    '''5-7단계'''
    if l == 0:
        return 'aaa'
    elif l >= 15:
        new_id = new_id[:15]
        if new_id[-1] != '.':
            return new_id
        else:
            return new_id[:-1]
    elif l == 1:
        return new_id + new_id[-1]*2
    elif l == 2:
        return new_id + new_id[-1]
    return new_id