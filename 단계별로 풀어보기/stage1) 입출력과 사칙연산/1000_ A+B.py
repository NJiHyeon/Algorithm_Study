# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
A, B = input().split()
print(int(A)+int(B))

# 풀이
    # input 함수로 입력받는 것은 문자열
    # 두개의 숫자를 입력받으면 split() 함수를 이용해서  쪼갠다.
        # ex) 3 9(단, A는 1보다 크고, B는 10보다 작아야 함)
    # 두개의 문자열을 숫자형으로 바꿔준 다음 더한다.
    
# 다른 풀이
A, B = map(int, input().split())
print(A+B)
