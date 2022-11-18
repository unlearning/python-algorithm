# 1.
def solution(n):
    answer = 0
    a = 1
    for i in range(1, n + 1):
        a *= i
        if a > n:
            return answer
        else:
            answer = i
            continue
    return answer

# 2.
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k