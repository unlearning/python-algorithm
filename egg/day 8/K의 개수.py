# K의 개수

# 내 풀이
def solution(i, j, k):
    answer = 0
    for m in range(i, j+1):
        answer += str(m).count(str(k))
    
    return answer

# 다른 사람 풀이
def solution(i, j, k):
    answer = sum([str(i).count(str(k)) for i in range(i, j+1)])
    return answer

# 다른 사람 풀이
from collections import Counter

def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        answer += Counter(str(n))[str(k)]
    return answer