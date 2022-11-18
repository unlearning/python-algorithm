# 7의 개수

# 내 풀이
def solution(array):
    answer = "".join((str(i) for i in array))

    return answer.count("7")

# 다른 사람 풀이
def solution(array):
    return ''.join(map(str, array)).count('7')