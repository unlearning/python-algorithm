# https://school.programmers.co.kr/learn/courses/30/lessons/120903

# 내 풀이
def solution(s1, s2):
    return len(list(filter(lambda x: x in s2, s1)))

# 다른 사람 풀이
def solution(s1, s2):
    return len(set(s1)&set(s2))
