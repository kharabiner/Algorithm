def safe(i, j, board):
    n = len(board)
    for r in range(3):
        for c in range(3):
            if 0 <= i+r < n and 0 <= j+c < n:
                if board[i+r][j+c] and board[i+r][j+c] == 1:
                    return False
    return True

def solution(board):
    answer = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if safe(i-1, j-1, board):
                answer += 1

    return answer