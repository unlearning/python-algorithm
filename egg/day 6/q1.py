# 문자열 정렬하기(1)

# 첫 번째 내 풀이
def solution(my_string):
    answer = []
    
    for i in my_string :
        if i.isdigit():
            answer.append(int(i))

    return sorted(answer)

# 두 번째 내 풀이
def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))
