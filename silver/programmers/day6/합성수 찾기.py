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
