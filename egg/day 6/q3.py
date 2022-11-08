# 대문자와 소문자

# 첫 번째 내 풀이
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else :
            answer += i.upper()
    return answer
print(solution("cC"))


# 다른 사람 풀이
def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])
