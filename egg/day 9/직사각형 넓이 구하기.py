# 직사각형 넓이 구하기

# 내 풀이
def solution(dots):
    answer = sorted(dots)  
    # [[1, 1], [2, 1], [2, 2], [1, 2]]를 정렬하면 
    # [[1, 1], [1, 2], [2, 1], [2, 2]]가 되는 것을 이용했습니다
    fnum = answer[2][0] - answer[0][0]
    snum = answer[1][1] - answer[3][1]
    return fnum * snum


# 다른 사람 풀이
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
