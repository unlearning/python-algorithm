# 2차원으로 만들기

# 내 풀이
def solution(num_list, n):
    answer = []

    for i in range(0, len(num_list), n):
        answer += [num_list[i:i+n]]

    return answer


# 다른 사람 풀이
def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]
