# https://school.programmers.co.kr/learn/courses/30/lessons/120848

# 내 풀이
def solution(n):
    step, now = 1, 1
    while True:
        now *= step
        if now > n:
            return step - 1
        step += 1

# 다른 사람 풀이
def solution(n):
    num,k = 1,1
    while(num<=n):
        num*=k
        k+=1
    return k-2