# 1.
def solution(my_string, n):
    mystr = ""
    for i in my_string:
        mystr += i * n
    return mystr

# 2.
def solution(my_string, n):
    return ''.join(i*n for i in my_string) # join(): 문자열 삽입
