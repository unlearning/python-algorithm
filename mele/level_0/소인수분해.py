# https://school.programmers.co.kr/learn/courses/30/lessons/120852

# 내 풀이
def solution(n):
    answer = []
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            answer.append(i)
            while n%i == 0:
                n /= i
    return answer if answer else [n]

# 다른 사람의 풀이
def prime_list(n):
    k = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n+1):
        if k[i]:
            primes.append(i)
            for j in range(2*i,n+1,i):
                k[j] = False
    return primes

def solution(n):
    result = []
    for prime in prime_list(n):
        if n%prime == 0:
            result.append(prime)
            while n%prime == 0:
                n/=prime
    return result