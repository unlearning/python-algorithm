# 1. 
def solution(my_string):
    collect = 'a', 'e', 'i', 'o', 'u'
    for i in collect:
        my_string = my_string.replace(i, '')
    return my_string

print(solution("bus"))

# 2. 
def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string

# 3.
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])

# 4.
import re

def solution(my_string):
    return re.sub(r"a|e|i|o|u", "", my_string)
