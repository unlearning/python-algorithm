# 숫자 찾기

# 첫 번째 내 풀이
def solution(num, k):
    answer = str(num)
    result = answer.find(str(k))
    if result != -1:
        return result+1
    else :
        return result

# 다른 사람 풀이
def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1
