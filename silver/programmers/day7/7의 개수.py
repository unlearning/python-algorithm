# 1.
def solution(array):
    count = 0
    for i in str(array): # [도 문자로 인식
        if i == '7':
            count += 1
    return count

# 2.
def solution(array):
    return ''.join(map(str, array)).count('7')

# 3.
def solution(array):
    return str(array).count('7')