# 숨어있는 숫자의 덧셈(2)

# 내 풀이
import re
def solution(my_string):

    for i in my_string:
        if i.isdigit():
            pass
        else:
            my_string = my_string.replace(i," ",1)


    answer = my_string.split()
    result = []

    for i in answer:
        result.append(int(i))

    return sum(result)


print(solution("aAb1B2cC34oOp"))

# 다른 사람 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

# 다른 사람 풀이
def solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])
