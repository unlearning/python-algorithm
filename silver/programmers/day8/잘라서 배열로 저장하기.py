# 1.
# [i for i in range(0, number, n)] : 0부터 my_str의 길이(16)까지 i를 6개씩 꺼냄
# i = [0, 6, 12]
# my_str[i:i+n] : my_str[0:6], my_str[6:12], my_str[12:18]

def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]

# 2.
def solution(my_str, n):
    answer = []

    while len(my_str) > n:
        answer.append(my_str[:n])
        my_str = my_str[n:]

    if my_str != "":
        answer.append(my_str)
    return answer