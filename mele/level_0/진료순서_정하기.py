# https://school.programmers.co.kr/learn/courses/30/lessons/120835

# 내 풀이
def solution(emergency):
    return [len(emergency) - emergency.index(n) for n in sorted(emergency)]

# 다른 사람 풀이
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]