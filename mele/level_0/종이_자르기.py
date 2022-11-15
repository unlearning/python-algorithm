# https://school.programmers.co.kr/learn/courses/30/lessons/120922

# 내 풀이
def solution(M, N):
    return M-1+M*(N-1)

# 다른 사람 풀이
def solution(M, N):
    return (M * N) - 1

# dfs 풀이
def get_cut_cnt_dfs(width, height):
    width, height = min(width, height), max(width, height)
    if width == 1 and height == 1:
        return 0
    return 1 + get_cut_cnt_dfs(width, height//2) + get_cut_cnt_dfs(width, height-height//2)
def solution(M, N):
    return get_cut_cnt_dfs(M, N)