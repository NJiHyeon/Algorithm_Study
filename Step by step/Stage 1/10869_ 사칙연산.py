# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
A, B = input().split()
def cal() : 
    print(int(A)+int(B))
    print(int(A)-int(B))
    print(int(A)*int(B))
    print(int(int(A)/int(B)))
    print(int(A)%int(B))
cal()


# 풀이
    # input 함수로 입력받는 것은 문자열
    # 두개의 숫자를 입력받으면 split() 함수를 이용해서  쪼갠다.
        # ex) 5 4 (단, A는 1보다 크고, B는 10보다 작아야 함)
    # 한번에 출력시키기 위해 함수로 묶는다.
    # 주의) 예시 출력에서 나누기를 하면 몫이 "자연수"가 나와야 하므로, 나누기를 하고 다시 int로 묶어준다.