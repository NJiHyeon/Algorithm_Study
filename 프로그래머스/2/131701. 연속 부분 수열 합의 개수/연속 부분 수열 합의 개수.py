def solution(elements):
    answer = 0
    p_elements = elements + elements[:len(elements)-2]
    nums = []
    for i in range(1, len(elements)+1) :
        for j in range(len(elements)) :
            sums = sum(p_elements[j:j+i])
            nums.append(sums)
        #nums = list(set(nums))
    answer+=len(list(set(nums)))
    return answer