# https://school.programmers.co.kr/learn/courses/30/lessons/120910

# 내 풀이
def solution(n, t):
    return n * 2**t

# 다른 사람 풀이
# TODO: 이해해보기
def solution(n, t):
    return n << t

# 은비's
def solution(n, t):
    total = n
    for i in range(t):
        total *= 2
    return total