## 1차원 배열
- for, while 등의 반복문을 사용

### 🔎 Fuction
- **`count`**
    - for문을 이용하여 변수를 1씩 추가해 개수를 세는 방법도 있지만, 파이썬에는 편리한 함수 존재
    - `list_name.count(count하고 싶은 숫자/문자)`

- **`max, min`**
    - 리스트에서 최댓값, 최솟값 찾기
    - `max(list_name)`, `min(list_name)`

- **`index`**
    - 특정 값의 인덱스 찾기
    - `list_name.index(값)`, `list_name.index(max(list_name))`, `list_name.index(min(list_name))`

- **`remove`**
    - 리스트에서 특정 값을 제거하고 싶을 때
    - `list_name.remove(값)`

- **`리스트 만들기`**
    - `list_name = [i for i in range(1, 20)]`

- **`set`**
    - 겹치는 것 빼기
    - `set(list_name)`
    
- **`역순처리`**
    - 전체 역순 : `list_name[::-1]`
    - 원하는 부분 역순 : `list_name[i-1:j] = n_list[j-1:i-2:-1]` (단, 이렇게 하면 인덱스 0까지 역순 처리가 되지 않는다. 따라서 i=0까지 원할 때는 `n_list[j-1::-1]`로 처리
    
----------------------------------
### 💡 Problem type


----------------------------------
### ✨Caution

----------------------------------
### 📌 Question to be solved again
- [10811번번](https://www.acmicpc.net/problem/10811번) : 맞았지만 시간이 오래 걸려서 한번 더 풀어보면 좋을듯 !