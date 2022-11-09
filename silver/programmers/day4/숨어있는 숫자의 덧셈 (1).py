# 1.
import re

def solution(my_string):
    answer = re.sub(r'[^0-9]', '', my_string)
    return sum(map(int, answer))

# 2. # list(filter(lambda x: x ==1, [1,2,3]))
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit()) # for문에 해당하는 각각의 원소가 if condition에 해당하는지, 아닌지
