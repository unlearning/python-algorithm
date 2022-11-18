# 중복된 문자 제거

# 내 풀이
def solution(my_string):
    answer = ""

    for i in my_string:
        if i not in answer:
            answer += i
    
    return answer

# 다른 사람 풀이
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
