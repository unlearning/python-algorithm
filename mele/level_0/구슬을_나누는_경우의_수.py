# https://school.programmers.co.kr/learn/courses/30/lessons/120840

# 내 풀이
def facto(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def solution(balls, share):
    return facto(balls)/facto(balls-share)/facto(share)

# ?
def solution(balls, share):
    answer = 1
    for i in range(share):
        answer *= (balls-i)
    for i in range(share):
        # answer /= (share-i) # 소수점 오차 발생
        answer //= (share-i)
    return answer

# 다른 사람 풀이
import math
def solution(balls, share):
    return math.comb(balls, share)

import math
def solution(balls, share):
    return math.factorial(balls)/(math.factorial(balls-share)*math.factorial(share))

def factorial(n):
    if n<2: return 1
    return n*factorial(n-1)
def solution(balls, share):
    return factorial(balls)/(factorial(balls-share)*factorial(share))