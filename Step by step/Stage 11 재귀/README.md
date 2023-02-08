## 재귀 : 재귀함수
- 규칙이 있는 수식을 반복해야 할 때 
- for문 대신으로도 많이 쓰인다.

### 🔎 Fuction
- `sys.setrecursionlimit(10 ** 6)`
    - 파이썬의 재귀 최대 깊이의 기본 설정이 1000회이기 때문에 런타임 에러가 발생하기 쉽다.
    - 따라서 위의 문제를 해결하기 위해 재귀 문제가 나오면 이걸 무조건 먼저 설정하고 풀기 !!!
- `join 함수`
    - `.join(list_name)` : 매개변수로 들어온 리스트를 문자열로 합쳐서 반환
    - `구분자.join(list_name)` : 리스트의 값과 값 사이에 구분자를 넣어서 하나의 문자열로 합쳐준다. 
        - `'.\n'.join(str_list_name)`
        - `'_'.join(str_list_name)`
        - `'.'.join(str_list_name)`

----------------------------------
### 💡 Problem type
- ⚠ 마지막에, return 함수 호출 [10870번](https://www.acmicpc.net/problem/10870), [10872번](https://www.acmicpc.net/problem/10872)
    - `return + 계산과정`을 생각하면 쉬움
    - 팩토리얼 계산 : `n*함수(n-1)`
    - 피보나치 계산 : `함수(n-1) + 함수(n-2)`

- ⚠ 마지막에, return 출력 결과(리스트,...) [2447번](https://www.acmicpc.net/problem/2447), [24060번](https://www.acmicpc.net/problem/24060), [25501번](https://www.acmicpc.net/problem/25501)
    - `def( ) :           `
    - `    if _____ :     `
    - `        return 숫자` # 맨 처음 시작 반환값
    - `    b = ...        ` # 함수 호출 때 사용할 변수 만들기 
    - `    a = def( )     ` # 함수 호출
    - `    L = [ ], 0     ` # 리셋 변수를 설정
    - `    while, if, for ` # 추가적인 처리
    - `    return ____    ` # 최종 return

- ⚠ 최소 단위 return의 위치
    - 대부분의 문제는 함수를 정의하고 바로 아래에 최소단위까지 왔을 때 하나의 값을 return하고 끝내도록 한다.
    - return을 하지 않고 계속 반복하도록 하는 문제도 있다. 

----------------------------------
### ✨Caution
- 파이썬에서 외부에 선언한 변수를 함수속에서 호출하고자 할때 아래와 같은 오류 발생
    - 원인 : 위 에러는 전역변수를 지역 변수로 호출했기 때문에 발생하며 
    - 해결법 : 간단하게 **함수 내부에 `global '변수명'` 을 추가**하면 해결 

----------------------------------
### 📌 Question to be solved again
- [2447번](https://www.acmicpc.net/problem/2447)
- [24060번](https://www.acmicpc.net/problem/24060)
- [11729번](https://www.acmicpc.net/problem/11729)