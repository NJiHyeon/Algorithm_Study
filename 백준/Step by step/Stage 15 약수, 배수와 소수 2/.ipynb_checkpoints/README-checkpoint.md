### 🔎함수
#### 최소공배수, 최대공약수
##### 기본함수
- `import math`
- `gcd` : 최대공약수
- `lcm` : 최소공배수

##### 리스트 안에서 찾기
def gcd_n(arr) : 
    gcd = arr[0]
    for item in arr :
        gcd = gcd_(gcd, item)
    return gcd
   

#### 소수 찾기(범위가 넓은)
##### math.sqrt(x) + 1까지만 확인하는 테크닉 이용
##### 아래의 함수 패턴은 외워두기
- `def sosu(x) :                               `
- `    for i in range(2, int(math.sqrt(x))+1) :`
- `        if x%i == 0 :                       `
- `            return False                    `
- `    return True                             `
