def solution(new_id):
    import re
    new_id1 = new_id.lower()
    
    new_id2 = re.sub('[^a-z0-9-_.]', '', new_id1)
    
    while '..' in new_id2:
        new_id2 = new_id2.replace('..', '.')
    new_id3 = new_id2
    
    if new_id3 and new_id3[0] == '.':
        if len(new_id3) == 1:
            new_id3 = ''
        else:
            new_id3 = new_id3[1:]
    if new_id3 and new_id3[-1] == '.':
        if len(new_id3) == 1:
            new_id3 = ''
        else:
            new_id3 = new_id3[:-1]
    new_id4 = new_id3
    
    if new_id4 == '':
        new_id4 = 'a'
    new_id5 = new_id4
        
    if len(new_id5) >= 16:
        new_id5 = new_id5[:15]
        if new_id5[-1] == '.':
            new_id5 = new_id5[:-1]
    new_id6 = new_id5
    
    while len(new_id6) <= 2:
        new_id6 += new_id6[-1]
    new_id7 = new_id6
    
    return new_id7
    

    return new_id3