## 기본수학2 : 소수와 기하
### 🔎 Fuction


----------------------------------
### 💡 Problem type
#### 1. 소수의 개수 출력 [1978번](https://www.acmicpc.net/problem/1978), [4948번](https://www.acmicpc.net/problem/4948)
- 기본적인 방법
    - 먼저 숫자가 들어있는 리스트 만들어주고 
    - `for x in numbers`문으로 하나씩 꺼내서 확인
    - 그 숫자에 대해 `i in range(2, x+1)`문으로 i가 2부터 x까지 확인하도록
        - 만약에 **x나누기 i가 0이면서 x와 i가 같으면 소수**
    - `sosu += 1`로 개수 더해주기
- n보다 크고 2n보다 작거나 같은 소수의 개수 출력
    - 주어진 범위 사이에서 소수를 모두 구해놓고, 입력받은 숫자 사이에서 소수의 개수를 출력하도록 구하기


#### 2. 소수 출력 [2581번](https://www.acmicpc.net/problem/2581),[1929번](https://www.acmicpc.net/problem/1929), [9020번](https://www.acmicpc.net/problem/9020)
- 주어진 숫자 사이에서 소수인 숫자들의 합 출력(`sosu_sum = 0` 만들어놓기)
- 그중에서 최소값(소수) 출력(`sosu_list = []` 만들어놓기)
- 두 수 사이에 있는 소수 모두 출력 (`int(i**0.5)+1` 여기까지만 확인)
- 두개의 소수를 출력해서 주어진 자연수 만들기

#### 3. 소인수 [11653번](https://www.acmicpc.net/problem/11653)
- 소수 출력하는 문제와 거의 비슷
- 단, for문을 돌면서 i가 무조건 커지는게 아니라 똑같은 수로 또 나눌 수 있으므로 `while 조건`문을 돌려서 나누어 떨어지는 것이 없을 때까지 반복한다. 
- ex. `while N % x == 0 :`

----------------------------------
### ✨Caution
- :star: `if문`이 끝나면 꼭 `break`로 제어문 풀어주기 !
- 몇개 받을지 모르는 숫자는 한줄에 여러개를 받아야 될 때
    - numbers = **list**(map(int, input().split()))를 이용해서 리스트 형태로 저장 !!
- 시간초과 문제 해결
    - `int(i**0.5)+1`
    - 주어진 범위에서 0 또는 1로된 리스트를 만들어 놓고, 소수이거나 소수가 아닌 숫자를 바꿔주는 형식으로 

----------------------------------
### 📌 Question to be solved again
[2581번](https://www.acmicpc.net/problem/2581)
[1929번](https://www.acmicpc.net/problem/1929)
[4948번](https://www.acmicpc.net/problem/4948)
[9020번](https://www.acmicpc.net/problem/9020)