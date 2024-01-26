def solution(n):
    result = ''
    while n :
        if n%3 != 0 :
            result += str(n%3)
        else :
            result += '4'
            n -= 1
        n //= 3
    return result[::-1]