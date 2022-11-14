#  첫 풀이
def solution(before,after):
  before= sorted(before)
  after=sorted(after)
  if before == after :
    return 1
  else:
    return 0

print(solution("olleh","hello"))
# 두 번 째 풀이
# def solution(before, after):
#     after="".join(list(reversed(list(before))))
#     if str(before) == str(after):
#       return 1
#     else :
#         return 0
