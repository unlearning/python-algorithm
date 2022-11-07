# https://school.programmers.co.kr/learn/courses/30/lessons/120836

# 내 풀이
def solution(n):
    return len(list(i for i in range(1, n+1) if (n/i).is_integer()))

# 다른 사람 풀이
def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))