# 문자열 밀기

# 내 풀이
def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if A == B:
            return answer
        A = A[-1] + A[:-1]
        answer += 1

    return -1 

# 다른 사람 풀이
def solution(A, B):
    #if A == "":
    #    return 0

    AA = A+A
    answer = AA.find(B)

    if answer >0:
        answer = len(A) - answer

    return answer

# 다른 사람 풀이
from collections import deque

def solution(A, B):
    a, b = deque(A), deque(B)
    for cnt in range(0, len(A)):
        if a == b:
            return cnt
        a.rotate(1)
    return -1