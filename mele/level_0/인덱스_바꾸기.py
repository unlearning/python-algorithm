# https://school.programmers.co.kr/learn/courses/30/lessons/120895

# 내 풀이
def solution(my_string, num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    return my_string[:num1] + my_string[num2] + my_string[num1+1:num2] + my_string[num1] + my_string[num2+1:]

# 다른 사람 풀이
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)
