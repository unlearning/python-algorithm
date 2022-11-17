# https://school.programmers.co.kr/learn/courses/30/lessons/120896

# 내 풀이
def solution(s):
    return "".join(sorted(c for c in s if s.count(c) == 1))

# 다른 사람 풀이
def solution(s):
    answer = ''
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(c) == 1:
            answer += c
    return answer

from collections import Counter
def solution(s):
    return ''.join(sorted([k for k, v in Counter(s).items() if v == 1]))