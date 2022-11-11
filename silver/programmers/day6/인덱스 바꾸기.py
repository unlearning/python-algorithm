# 1.
def solution(my_string, num1, num2):
    l_string = list(my_string)
    l_string[num1], l_string[num2] = l_string[num2], l_string[num1]
    return ''.join(map(str, l_string)) # 리스트 → 문자열
