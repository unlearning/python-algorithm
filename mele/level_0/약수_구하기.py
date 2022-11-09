# https://school.programmers.co.kr/learn/courses/30/lessons/120897

# 내 풀이
def solution(n):
    return [d for d in range(1, int(1 + n * .5)) if n % d == 0] + [n]