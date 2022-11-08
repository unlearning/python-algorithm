# https://school.programmers.co.kr/learn/courses/30/lessons/120909

# 내 풀이
def solution(n):
  sqrt = n**(1 / 2)
  return 1 if sqrt == int(sqrt) else 2

# 다른 사람 풀이
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

# 승민's
def solution(n):
    result = 0
    for i in range(1, 1001):
        result = i ** 2
        if result == n:
            return 1

    return 2