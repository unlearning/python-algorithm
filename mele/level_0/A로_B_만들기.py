# https://school.programmers.co.kr/learn/courses/30/lessons/120886

# 내 풀이
def solution(before, after):
    return int(sorted(list(before)) == sorted(list(after)))

# 다른 사람 풀이
def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0