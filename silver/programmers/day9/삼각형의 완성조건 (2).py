# 1.
# keypoint
# 1) 가장 긴 변의 길이는 나머지 두 변의 길이의 합보다 작음
# 2) 수학 공식 존재

def solution(sides):
    max_answer = max(sides[0], sides[1]) # 음수가 나오지 않기 위해서 max()/min() 과정 수행
    min_asnwer = min(sides[0], sides[1])
    return (max_answer + min_asnwer) - (max_answer - min_asnwer) - 1 # 중복되는 값 - 1

# 2.
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1 # Q.