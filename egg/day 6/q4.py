# 중앙값 구하기

# 첫 번째 내 풀이
def solution(array):
    array.sort()
    answer = array.index(max(array))
    answer = int(answer / 2)

    return array[answer]

# 두 번째 내 풀이
def solution(array):
    array.sort()
    answer = len(array) // 2

    return array[answer]

# 다른 사람 풀이
def solution(array):
    return sorted(array)[len(array) // 2]
