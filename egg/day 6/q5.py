# 약수 구하기

# 첫 번째 내 풀이
def solution(n):
    answer = []

    for i in range(1, n+1):
        if n % i == 0:
            answer += divmod(n, i) # answer += n // i
    answer = set(answer) # 제거
    answer.remove(0) # 제거

    return sorted(answer)

# 두 번째 내 풀이
def solution(n):
    return sorted(filter(lambda x: n % x == 0 , range(1, n+1) ))

print(solution(24))


# 다른 사람 풀이
def solution(n):
    answer = [i for i in range(1, n+1) if n % i == 0]
    return answer
