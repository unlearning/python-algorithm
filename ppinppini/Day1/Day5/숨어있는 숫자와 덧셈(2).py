# import re
# def solution(my_string):

#   numbers= re.sub(r'[^0-9]','',my_string)
#   for i in my_string:
#     if i in numbers:
#         i=i+i
#   return i
# print(solution("aAb1B2cC34oOp"))

import re
my_string="aAb1B2cC34oOp"
numbers= re.sub(r'[^0-9]','',my_string)
print(list(numbers))


