# 1.
import re

def solution(my_string):
    answer = re.sub(r'[^0-9]', '', my_string)
    return sum(map(int, answer))

# 2.
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit()) # 정확한 실행 순서?
