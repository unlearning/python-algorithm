# 1.
# ex. [[80, 70], [90, 50], [40, 70], [50, 80]]

def solution(score):
    average = [] # Q. 평균 변수 이름으로 average 괜찮나요?
    answer = []
    for grade in score:
        average.append(sum(grade) // len(grade))
    average = sorted(average, reverse=True)
    # print(average) : [75, 70, 65, 55]
    for grade in score:
        answer.append(average.index(sum(grade) // len(grade))) # Q. [[1, 2], [1, 1], [1, 1]] : [1, 1, 1]을 어떻게 처리할지 궁금합니다.
    return [idx + 1 for idx in answer] # = list(map(lambda idx: idx + 1, answer))