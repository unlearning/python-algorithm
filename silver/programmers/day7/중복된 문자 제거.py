# 1.
# point: list, not in
# 2번째부터 반복되는 문자 제외
def solution(my_string):
    answer = []
    l_m = list(my_string)
    for i in l_m:
        if i not in answer:
            answer.append(i)
    return ''.join(answer)

# 2.
# 문자열에서도 not in → 중복되지 않는 문자 빈 문자열에 추가
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer