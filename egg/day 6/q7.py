# 가장 큰 수 찾기

# 첫 번째 내 풀이
def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer

# 다른 사람 풀이
def solution(array):
    answer = [max(array), array.index(max(array))]
    return answer
