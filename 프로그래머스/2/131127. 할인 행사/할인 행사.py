def solution(want, number, discount):
    import collections
    answer = 0
    discount_dict = collections.Counter(discount)
    want_dict = dict(zip(want, number))
    
    # 수량과 품목이 있는지 확인
    max_num = max(number)
    max_want = want[number.index(max(number))] #'banana'
    if (max_want not in list(set(discount))) or (discount_dict[max_want] < max_num) :
        answer = 0
    
    # 연속해서 가능한지 확인
    else :
        for i in range(len(discount)-9) :
            discount_dict_10 = collections.Counter(discount[i:i+10])
            discount_dict_10 = dict(sorted(discount_dict_10.items()))
            want_dict = dict(sorted(want_dict.items()))
            if want_dict == discount_dict_10 :
                answer += 1
    return answer