# https://school.programmers.co.kr/learn/courses/30/lessons/120837

# 내 풀이
def solution(hp):
    a, b = divmod(hp, 5)
    c, d = divmod(b, 3)
    return a+c+d

# 다른 사람 풀이
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)