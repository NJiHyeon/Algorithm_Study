def solution(n, wires):
    answer = []
    for i in range(len(wires)) :
        wire2 = wires.copy()
        wi = wire2.pop(i)
        a = [wi[0]]
        b = [wi[1]]

        while wire2 :
            w = wire2.pop(0)
            if w[0] in a :
                a.append(w[1])
            elif w[1] in a :
                a.append(w[0])
            elif w[0] in b :
                b.append(w[1])
            elif w[1] in b :
                b.append(w[0])
            else :
                wire2.append(w)
        answer.append(abs(len(a)-len(b)))
    return min(answer)