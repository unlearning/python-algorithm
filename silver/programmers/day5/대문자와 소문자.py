# 1.
def solution(my_string):
    answer = ""
    for i in my_string:
        if i.islower():
            answer += i.upper()
        else:
            answer += i.lower()
    return answer

# 2.
def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])

# 3.
def solution(my_string):
    return ''.join([i.lower() if ord(i)<ord('a') else i.upper() for i in my_string ])
