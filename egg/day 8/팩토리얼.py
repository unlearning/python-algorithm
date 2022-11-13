# 팩토리얼

# 내 풀이
def solution(n):

    for i in range(1, 12):
        temp = 1
        for j in range(1, i+1):
            temp *= j
        if (temp > n):
            return i-1
            break


# 다른 사람 풀이
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k