# 1.
def solution(n, numlist):
    return [i for i in numlist if i % n == 0]

# 2.
def solution(n, numlist):
    return list(filter(lambda x: x % n == 0, numlist))
