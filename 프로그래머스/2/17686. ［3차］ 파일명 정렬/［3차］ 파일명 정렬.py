def solution(files):
    import re
    answer = []
    file = dict()
    for f in files :
        numbers = re.findall(r'\d+', f) #정규식으로 숫자만 뽑아내기
        index = f.index(numbers[0][0])  #숫자가 처음 나타나는 인덱스 확인
        #파일명:[HEAD, NUMBER] 딕셔너리 만들기
        file[f] = [f[:index].lower()]   #그 인덱스까지 HEAD
        file[f].append(int(numbers[0])) #숫자만 뽑아낸 리스트에서 TAIL 부분의 숫자가 같이 들어가있으므로 NUMBER 부분 (하나의 숫자)만 뽑기 위해 0번 인덱스 추출
    file_s = dict(sorted(file.items(), key=lambda x: (x[1][0], x[1][1]))) #정렬
    answer = list(file_s.keys())
    return answer