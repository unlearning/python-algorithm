# 외계행성의 나이

# 첫 번째 내 풀이
def solution(age):
    answer = str(age)
    result = list(map(lambda x: chr(int(x)+97), answer))
    return "".join(result)

# 다른 사람 풀이
def solution(age):
    str_age = str(age)
    answer = ''
    lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for ch in str_age:
        for i in range(0, 10):
            if int(ch) == i:
                answer += lst[i]
    return answer
