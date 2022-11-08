# https://school.programmers.co.kr/learn/courses/30/lessons/120823

# 내 풀이
n = int(input())
[print("*" * i) for i in range(1, n + 1)]

# 다른 사람 풀이
n = int(input())
print("\n".join(["*" * (i+1) for i in range(n)]))