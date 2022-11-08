# 1.
def solution(array):
    answer = [0,0]
    answer[0] = max(array)
    answer[1] = array.index(max(array)) # sorted, reversed와 같이 반환값 o
    return answer

# 2.
def solution(array):
    return [max(array), array.index(max(array))]
