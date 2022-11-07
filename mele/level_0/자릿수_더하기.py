# https://school.programmers.co.kr/learn/courses/30/lessons/120906

# 내 풀이
def solution(n):
    return sum(map(int, list(str(n))))

# 다른 사람 풀이
def solution(n):
    answer = 0
    while n:
        answer += n%10
        n //= 10
    return answer
    
def solution(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer