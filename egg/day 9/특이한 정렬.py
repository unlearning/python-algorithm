# 특이한 정렬

# 내 풀이
def solution(numlist, n):
    answer = []
    answers = sorted([[abs(i - n), numlist.index(i)] for i in numlist])
    print(answers)
    stack = answers[1][1]
    stack2 = answers[1][0]
    count = 1
    total = 0

    for i in answers:
        # for j in range(1, 2):
            if stack2 == i[0]:
                # if total == 1:
                #     pass
                if stack > i[1]:
                    answer.append(numlist[stack])
                    # answers.pop(numlist[stack])
                    stack = answers[count][1]
                    answer.append(numlist[stack])
                    answers.pop(numlist[stack])
                    total = 1
                    print(answer)
                    pass
            else:
                answer.append(numlist[i[1]])
                stack = answers[count + 1][1]
                stack2 = answers[count + 1][0]
                total = 0

    return answer


print(solution([1, 2, 3, 4, 5, 6], 4))

