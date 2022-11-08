# 1.
def solution(my_string):
    return sorted(list(map(int, (i for i in my_string if i.isdigit()))))

# 2.
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])

# 3.
import re

def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))
