# 1.
# keypoint
# 1) 직사각형의 넓이
# (가장 큰 x 값 - 가장 작은 x 값) * (가장 큰 y 값 - 가장 작은 y 값)
# 2) min()/max() : iterable한 객체에만 적용 가능
# ex. for i in dots: print(max(i[0])) → i[0]이 정수형이므로 적용 불가
# 3) 2차원 배열에서 min()/max() 사용 시 첫 번째 요소를 기준으로 결과 출력
# ex. [[1,2,3], [0,4,5]] → max() → [1,2,3] 출력

def solution(dots):
    min_x = min(i[0] for i in dots) # ex. min() 안에서 for문 진행, 즉 동시 진행 → 적용 가능
    max_x = max(i[0] for i in dots)
    min_y = min(i[1] for i in dots)
    max_y = max(i[1] for i in dots)
    return (max_x - min_x) * (max_y - min_y)

# 2.
def solution(dots):
    print(dots[0])
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1]) # max(dots)[0]: 양의 정수 x의 최댓값(오른쪽 끝 점)

# 3.
def solution(dots):
    x, y = [], [] # min()/max()를 적용하기 위해 iterable 객체 중 하나인 list 선언
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
    return (max(x) - min(x)) * (max(y) - min(y))