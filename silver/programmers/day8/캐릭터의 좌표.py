# 1.
def solution(keyinput, board):
    answer = [0, 0] # 1) board의 정중앙, 즉 입력에 따라 움직일 원점
    min_x, max_x = -(board[0] // 2), board[0] // 2 # 2) board의 값을 이용해 원점이 움직일 새로운 좌표를 그려야 함
    min_y, max_y = -(board[1] // 2), board[1] // 2 # 3) 좌표이므로 음수, 양수 값을 받을 변수 생성

    for i in keyinput:
        if (i == "up" and answer[1] < max_y):
            answer[1] += 1
        elif (i == "down" and min_y < answer[1]):
            answer[1] += -1
        elif (i == "left" and min_x < answer[0]):
            answer[0] += -1
        elif (i == "right" and answer[0] < max_x):
            answer[0] += 1
    return answer

# 2.
def solution(keyinput, board):
    answer = [0, 0]
    input = {"up":[0, 1], "down":[0, -1],
            "left":[-1, 0], "right":[1, 0]}
    min_x, max_x = -(board[0] // 2), board[0] // 2 
    min_y, max_y = -(board[1] // 2), board[1] // 2 
    
    for key in keyinput:
        if (key == "right" and answer[0] < max_x) or (key == "left" and min_x < answer[0]):
            answer[0] += input[key][0]
        if (key == "up" and answer[1] < max_y) or (key == "down" and min_y < answer[1]):
            answer[1] += input[key][1]    
    return answer
