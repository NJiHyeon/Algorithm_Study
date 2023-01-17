### 🔎 Fuction
#### 1️. `math.ceil(변수)`
- 숫자를 올림하는 함수
- `import math` 
- [2869번](https://www.acmicpc.net/problem/2869)

#### 2. `sys.stdin.readline().split()`
- 한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야 할 때
- `input()`으로 입력 받는다면 런타임에러가 발생한다. 
- `split()`은 상황에 따라 넣어주기
- `import sys` 

#### 3. `new_list.copy()`
- 새로운 리스트를 복사하는 함수
- `origin_list = new_list.copy()` 이런 식으로 많이 사용

----------------------------------
### 💡 Idea
#### 1️. 주기 이용 
- 어떤 문제 : 반복을 하긴 하는데 숫자가 점점 커지거나 점점 작아지고 주기에 맞는 숫자를 구해야 할 때(몇바퀴 ?, 몇바퀴 돌때 위치 어디 ?, 돌면서 X, Y값 구하기 ? 등등)
- 대부분 알고리즘
    - 1) 초기 값 : 만들어진 값(number, c_n 등), 주기 돌 변수(circle, n 등) 만들어서 숫자 지정
    - 2) While 문으로 입력값이 만들어진 값보다 크면 계속 반복 이런식으로
    - 3) number값은 `그 전값 + 배수*circle` 또는 `그 전값 + circle`으로 점점 커진다. ➡ `number += circle`
    - 4) circle값은 한바퀴 돌때마다 1씩 더해간다.
    - 5) 원하는 결과 출력하도록
- 주의할 점
    - 더하기 뿐만 아니라 빼기, 곱하고 더하기, 곱하고 빼기 등으로 만들 수도 있다. 
    - 그 전값 + alpha라는 모양을 기억 !
- [2292번](https://www.acmicpc.net/problem/2292), [1193번](https://www.acmicpc.net/problem/1193), [2839번](https://www.acmicpc.net/problem/2839)

#### 2️. 층별로 누적합 구해서 마지막 층의 숫자 구하기
- 누적합을 구할 때 
    - `new_list.append(sum(origin_list[:n+1]))` : 리스트를 이용해서 더해서 새로운 리스트에 넣어주기
- 원래 리스트를 새로운 리스트로 바꾸고 싶을 때
    - `origin_list = new_list.copy()`
- [2275번](https://www.acmicpc.net/problem/2775)



----------------------------------
### ✨Caution
#### 1️. 나눗셈(몫, 나머지)
- 나눗셈을 해서 몫과 나머지를 이용해 그 값으로 문제 풀이에 이용한다면 꼭 **나머지가 0** 일때를 주의해서 값 적용하기
- `if`, `else` 이용해서 상황별로 나눠주기
- [10250번](https://www.acmicpc.net/problem/10250)

#### 2. Input값 받을 때
- for문 안에 들어가서 받는지, 밖에서 전체 값을 받는지 잘 확인
- `int(input().split())` 불가능
    - int 함수는 리스트를 정수형으로 바꿀수 없기 때문
- 값을 받는 여러가지 유형
    - `A, B, C = intput().split()` : 두개의 입력값을 받을 때(문자형)
    - `A, B, C = map(int, input().split())` : 두개의 입력값을 받고 숫자로 바로 바꾸고 싶을 때(숫자형)
    - `list(map(int, str(input())))` : 숫자를 받고 각 자릿수가 필요할 때
    - 참고) `age = intput("당신의 나이는 ? :")`도 가능


----------------------------------
### 📌 Question to be solved again
[2275번](https://www.acmicpc.net/problem/2775)
[1193번](https://www.acmicpc.net/problem/1193)
[2839번](https://www.acmicpc.net/problem/2839)