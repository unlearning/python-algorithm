# https://school.programmers.co.kr/learn/courses/30/lessons/120813

# 내 풀이
def solution(n):
  return list(filter(lambda x: x % 2, range(n+1)))

# 다른 사람 풀이
def solution(n):
    return [i for i in range(1, n+1, 2)]