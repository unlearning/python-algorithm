# https://school.programmers.co.kr/learn/courses/30/lessons/120891

# 내 풀이
def solution(order):
    return len(list(n for n in str(order) if n in '369'))

# 다른 사람 풀이
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))