# 1.
# keypoint
# Z 바로 전 값 = 마지막 값 제거 : pop()

def solution(s):
    answer = []
    for i in s.split(): # for문에 split() 즉시 적용 가능
        if i == "Z":
            answer.pop()
        else:
            answer.append(int(i)) # str → int 즉시 적용 가능
    return sum(answer)