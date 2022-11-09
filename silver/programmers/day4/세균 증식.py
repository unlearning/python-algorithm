# 1.
def solution(n, t):
    total = n
    for i in range(1, t+1): # for i range(t)
        if i <= t: # 생략 가능
            total *= 2
    return total

# 2.
def solution(n, t):
    return n*(t**2)

# 3.
def solution(n, t):
    return n << t
