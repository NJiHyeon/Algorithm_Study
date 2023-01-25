### 🔎 Fuction
- `numbers = **list**(map(int, input().split()))`

----------------------------------
### 💡 Problem type
- 기본적인 유형 [2566번](https://www.acmicpc.net/problem/2566), [2738번](https://www.acmicpc.net/problem/2738)
    - 입력받을 때는 row만 for문으로 돌리고, col 숫자들은 list 형태로 입력받기
    - 확인할 때는 for문을 row, col 두번 돌리면서 확인
- x, y 좌표가 나올 때는 2차원 배열이 아닌지 ?! 생각
- 넓이 계산 [2563번](https://www.acmicpc.net/problem/2563)
    - 단순히 넓이 계산이 아닐 수 있다. (특히, 겹치는 부분이 있으면 주의)
    - 주어진 범위를 돌면서 0에서 1로 바꾼 뒤, 1의 개수 세는 방법 (단 범위가 100)




----------------------------------
### ✨Caution
- N행 M열이랑 인덱스 위치는 다르므로 주의하기

----------------------------------
### 📌 Question to be solved again
[2563번](https://www.acmicpc.net/problem/2563)