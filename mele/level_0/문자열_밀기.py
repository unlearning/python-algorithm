# https://school.programmers.co.kr/learn/courses/30/lessons/120921

# 내 풀이
def solution(A, B):
    for i in range(len(A)):
        if A == B[i:]+B[:i]:
            return i
    return -1

# 다른 사람 풀이
def solution(A, B):
    return (B*2).find(A)

from collections import deque
def solution(A, B):
    a, b = deque(A), deque(B)
    for cnt in range(0, len(A)):
        if a == b:
            return cnt
        a.rotate(1)
    return -1