# 1.
def solution(n, t):
    total = n
    for i in range(1, t+1):
        if i <= t:
            total *= 2
    return total

# 2.
def solution(n, t):
    return n*(t**2)

# 3.
def solution(n, t):
    return n << t
