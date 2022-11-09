# 피자 나눠 먹기(2)

import math
# math.gcd: 최대공약수를 구하는 함수

# 첫 번째 내 풀이
def solution(n):
    answer = math.gcd(6, n)
    return (6//answer)*(n//answer)*answer

# 두 번째 내 풀이
def solution(n):
    answer = math.gcd(6, n)
    if n % answer == 0:
        return n // answer
    else:
        return n

# 세 번째 내 풀이
def solution(n):
    answer = math.gcd(6, n) 
    result = [n//answer if n % answer == 0 else n]
    return result.pop(0)


# 다른 사람 풀이
def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6
