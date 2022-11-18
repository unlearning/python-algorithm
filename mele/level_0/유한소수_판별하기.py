# https://school.programmers.co.kr/learn/courses/30/lessons/120878

# 내 풀이
import math
def solution(a, b):
    b //= math.gcd(a, b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    return 1 if b == 1 else 2

# 다른 사람 풀이
def solution(a, b):
    return 1 if a/b * 1000 % 1 == 0 else 2