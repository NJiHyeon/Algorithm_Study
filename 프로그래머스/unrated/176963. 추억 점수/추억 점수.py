#name = ["may", "kein", "kain", "radi"]
#yearing = [5, 10, 1, 3]
#photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

def solution(name, yearing, photo) :
    result = []
    for group in photo : 
        score = 0
        for person in group :
            if person in name :
                i = name.index(person)
                score += yearing[i]
        result.append(score)
    return result
