# https://school.programmers.co.kr/learn/courses/30/lessons/120815

# 내 풀이
def lcm(x, y):
    if x < y:
        x, y = y, x
    _, z = divmod(x, y)
    return y if z == 0 else lcm(y, z)

def gcd(x, y):
    return x * y / lcm(x, y)

def solution(n):
    return gcd(6, n) / 6

# 다른 사람 풀이
import math
def solution(n):
    return (n * 6) / math.gcd(n, 6) / 6

def solution(n):
    answer = 1
    while 6 * answer % n:
        answer += 1
    return answer

def solution(n):
    return [n / k for k in [1,2,3,6] if n%k == 0][-1] 