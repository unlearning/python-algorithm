# 1.
import math

def solution(n):
    m = int(math.sqrt(n))
    return 1 if n == pow(m, 2) else 2

# 2.
import math

def solution(n):
    return 1 if int(math.sqrt(n)) ** 2 == n else 2