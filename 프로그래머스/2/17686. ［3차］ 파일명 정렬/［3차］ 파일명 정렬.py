def solution(files):
    import re
    answer = []
    file = dict()
    for f in files :
        numbers = re.findall(r'\d+', f)
        index = f.index(numbers[0][0])
        file[f] = [f[:index].lower()]
        file[f].append(int(numbers[0]))
    file_s = dict(sorted(file.items(), key=lambda x: (x[1][0], x[1][1])))
    answer = list(file_s.keys())
    return answer