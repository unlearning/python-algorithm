# 1.
def solution(n, k):
    k = k - (n // 10)
    return n * 12000 + k * 2000

# 2.
def solution(n, k):
    return n * 12000 + (k - n // 10) * 2000