# 인덱스 바꾸기

# 첫 번째 내 풀이
def solution(my_string, num1, num2):
    result =list(my_string)
    answer = my_string[num1]
    result[num1] = my_string[num2]
    result[num2] = answer
    return "".join(result)

# 다른 사람 풀이
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)
