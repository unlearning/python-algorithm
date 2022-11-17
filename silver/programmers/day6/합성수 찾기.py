# 1.
# 1과 소수를 제외한 모든 자연수가 합성수
def solution(n):
    count = n-1
    for i in range(2,n+1):
        for x in range(2,i):
            if i % x == 0:
                count -= 1
                break
    return n - 1 - count

# 2.
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output