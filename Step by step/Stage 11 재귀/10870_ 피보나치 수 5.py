n = int(input())
def pib(n) : 
    if n == 0 : 
        return 0
    elif 1<= n <= 2 :
        return 1
    return pib(n-1) + pib(n-2)

print(pib(n))