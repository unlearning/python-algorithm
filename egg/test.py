# 문자열 뒤집기
def solution(my_string):
    return my_string[::-1]

# 아이스 아메리카노

def solution(money):
    answer = [0, 0]
    answer[0] = money // 5500
    answer[1] = int(money % 5500)
    return answer
