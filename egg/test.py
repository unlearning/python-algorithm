# 문자열 뒤집기
def solution(my_string):
    return my_string[::-1]

# 아이스 아메리카노

def solution(money):
    answer = [0, 0]
    answer[0] = money // 5500
    answer[1] = int(money % 5500)
    return answer

# 피자 나눠 먹기
def solution(slice, n):

    answer = 0
    if n % slice == 0:
        answer = n//slice
    else :
        answer = n//slice + 1
    return answer

# 피자 나눠 먹기 저번 설명
def solution(slice, n):
    return (n-1)//slice +1


# 점의 위치 구하기

def solution(dot):
    answer = 0

    if dot[0] < 0 :
        if dot[1] < 0 :
            answer = 3
        else :
            answer = 2
    else :
        if dot[1] < 0 :
            answer = 4
        else :
            answer = 1
            
    return answer


