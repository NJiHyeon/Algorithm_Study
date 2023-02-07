### 재귀 : 재귀함수
### 🔎 Fuction
- `sys.setrecursionlimit(10 ** 6)`
    - 파이썬의 재귀 최대 깊이의 기본 설정이 1000회이기 때문에 런타임 에러가 발생하기 쉽다.
    - 따라서 위의 문제를 해결하기 위해 재귀 문제가 나오면 이걸 무조건 먼저 설정하고 풀기 !!!


----------------------------------
### 💡 Problem type
- 💡 마지막에, return 함수 호출 [10870번](https://www.acmicpc.net/problem/10870), [10872번](https://www.acmicpc.net/problem/10872)
    - `return + 계산과정`을 생각하면 쉬움
    - 팩토리얼 계산 : `n*함수(n-1)`
    - 피보나치 계산 : `함수(n-1) + 함수(n-2)`

- 💡 마지막에, return 출력 결과(리스트,...) [2447번](https://www.acmicpc.net/problem/2447), [24060번](https://www.acmicpc.net/problem/24060), [25501번](https://www.acmicpc.net/problem/25501)
    - `def( ) :           `
    - `    if _____ :     `
    - `        return 숫자` # 맨 처음 시작 반환값
    - `    b = ...        ` # 함수 호출 때 사용할 변수 만들기 
    - `    a = def( )     ` # 함수 호출
    - `    L = [ ], 0     ` # 리셋 변수를 설정
    - `    while, if, for ` # 추가적인 처리
    - `    return ____    ` # 최종 return



----------------------------------
### ✨Caution
- 파이썬에서 외부에 선언한 변수를 함수속에서 호출하고자 할때 아래와 같은 오류 발생
    - 원인 : 위 에러는 전역변수를 지역 변수로 호출했기 때문에 발생하며 
    - 해결법 : 간단하게 **함수 내부에 `global '변수명'` 을 추가**하면 해결 

----------------------------------
### 📌 Question to be solved again
- [2447번](https://www.acmicpc.net/problem/2447)
- [24060번](https://www.acmicpc.net/problem/24060)