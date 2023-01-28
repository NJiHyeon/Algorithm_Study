## 정렬 : 배열의 원소를 순서대로 나열하는 알고리즘
### 🔎 Fuction
#### **`map`**
- `map(int, input().split())` 
    - 입력값을 몇 개 받을지 알고, 그 값들을 공백으로 분리
    - 대부분 input()을 받는 형식이고 for문으로 반복하면서 받을 수도 있음
- `list(map(int, input().split()))` 
    - 숫자 입력값을 받아야 하는데 for문으로 받지 않을 때
    - 한꺼번에 받고 공백으로 분리 후, 리스트에 저장
- str 있는 거  

#### **`sys`**
- `list_name.append(int(sys.stdin.readline()))`
    - 범위가 커지면 시간초과가 발생할 수 있으므로 input() 대신 사용하면 유용

#### **`sort`**
- `list_name.sort()` 
    - 리스트 객체 자체를 정렬해주는 함수로 리스트에만 사용 가능
    - 기본적으로 리스트를 오름차순으로 정렬해주는 기능
    - 숫자, 소문자 문자, 대소문자 문자 리스트 모두 가능
    
- `reverse = False, True`
    - 리스트 정렬 방식을 지정해 줄 수 있는 옵션
    - True로하면 내림차순, False로하면 오름차순

- `sorted`와 비교
    - sorted는 새로운 정렬된 리스트를 반환하는 함수로 원본 리스트 값은 유지되고, 정렬된 새로운 리스트에 저장된다. (`a2=sorted(a1)`)
    - sort 함수는 원본 리스트 값이 정렬된 값으로 수정되어 출력되서 정렬된 값(새로운 변수)는 리턴되지 않는다.(`a1.sort()`)


#### **`반올림, 내림, 올림`**
- 반올림
    - `round(3.1415)`, `round(3.1415, 2)`, `round(3.1415, -1)`
- 올림
    - math 모듈 사용
    - `math.ceil(3.14)`, `math.ceil(-3.14)`
- 내림
    - math 모듈 사용
    - `math.floor(3.14)`, `math.floor(-3.14)` : 무조건 아래만 향해 내림한다. 
    - `math.trunc(-3.14)` : 내림을 하더라도 0으로 향한다.(int()와 같이 결과를 반환)

#### **`index`**
- `list_name.index(max(list_name))` : 리스트에서 최댓값의 인덱스 찾기
- `list_name.index(min(list_name))` : 리스트에서 최솟값의 인덱스 찾기




----------------------------------
### 💡 Problem type
- 정렬 종류
    - 버블 정렬 : 현재 값과 다음 인덱스의 값을 비교해서, 다음 인덱스 값이 현재 값보다 작으면 두 값을 서로 교환
    - 삽입 정렬 : 이전 인덱스의 값과 현재 인덱스의 값을 비교해 작은 값을 앞으로 옮긴다. 
    - 카운팅 정렬
    - 병합 정렬, 힘 정렬 ...

- 여러가지 방법들
    - `int(input())`로 받아서 sort()후 for문으로 print [2750번](https://www.acmicpc.net/problem/2750)
    - `int(sys.stdin.readline())`로 받아서 sort()후 for문으로 print [2751번](https://www.acmicpc.net/problem/2751)
    - `int(sys.stdin.readline())`와 배열 생성의 조합 [10989번](https://www.acmicpc.net/problem/10989)
       - 배열에는 각 숫자의 개수가 들어가게 된다.
       - 숫자의 수만큼 출력해 주도록 한다. 



----------------------------------
### ✨Caution




----------------------------------
### 📌 Question to be solved again
[10989번](https://www.acmicpc.net/problem/10989)