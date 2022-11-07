# https://school.programmers.co.kr/learn/courses/30/lessons/120889

# 내 풀이
def solution(sides):
    return 1 if max(sides) < sum(sides) - max(sides) else 2

# 다른 사람 풀이
def solution(sides):
    sides.sort()
    return 1 if sides[0]+sides[1]>sides[2] else 2