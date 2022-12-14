# keypoint
# 문자열 연결(+ or *) 이용
# ex. A + A = hellohello
# ex. A * 2 = hellohello

# 1. Why not?
def solution(A, B):
    answer = ''
    
    for i in range(1, len(A) + 1):
        if A[-i:] + A[0:-i] == B:
            # print(A[-1:], A[0:-1]) → o hell
            print(A[-2:], A[0:-2])
            # print(A[-2:], A[0:-2]) → lo hel
            return i
        elif A == B:
            return 0
        else:
            return -1

# 2.
def solution(A, B):
    for j in range(len(A)):
        temp = ''
        for i in range(len(A)):
            temp += A[i-j]
        print(temp)
        if temp == B:
            return j
    else:
        return -1

# 3.
# keypoint
# def solution(A, B) 함수에 직접 lambda 함수를 적용
solution = lambda a, b : (b * 2).find(a)

# 4.
def solution(A, B):
    #if A == "":
    #    return 0

    AA = A * 2
    answer = AA.find(B)

    if answer > 0:
        answer = len(A) - answer

    return answer