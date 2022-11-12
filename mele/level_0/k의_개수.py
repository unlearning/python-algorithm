# https://school.programmers.co.kr/learn/courses/30/lessons/120887

# 내 풀이
def solution(i, j, k):
    return "".join(map(str,range(i, j+1))).count(str(k))

# 다른 사람 풀이
def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer

def solution(i, j, k):
    return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))