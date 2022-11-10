# 나의풀이
def solution(n):
    answer = 0
    for i in range(1,n+1):
      if n%i ==0:
        answer+=i
      return (len(str(answer))>=3)

print(solution(10))