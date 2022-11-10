# https://school.programmers.co.kr/learn/courses/30/lessons/120846

# 내 풀이
def prime_len(n):
    nums = [False]*2+[True]*(n-1)
    for i in range(2, int(n**(1/2))+1):
        if nums[i]:
            for j in range(2*i, n+1, i):
                nums[j] = False
    return len([num for num in nums if num])

def solution(n):
    return n-prime_len(n)-1
    
# 다른 사람 풀이
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output