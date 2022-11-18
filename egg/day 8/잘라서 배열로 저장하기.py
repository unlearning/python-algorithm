# 잘라서 배열로 저장하기

# 내 풀이
def solution(my_str, n):
    answer = []
    i = 0

    while (n*(i+1) <= len(my_str)-1):
        answer.append(my_str[n*i : n*(i+1)])
        i += 1

    answer.append(my_str[n*i: n*(i+1)])
    return answer

# 다른 사람 풀이
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]

