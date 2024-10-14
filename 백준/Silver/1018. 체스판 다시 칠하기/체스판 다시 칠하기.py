N, M = map(int,input().split())
board = [input() for _ in range(N)]

def checkBoard(x,y):
    w_cnt = 0
    b_cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if board[x+i][y+j] == 'W':
                    b_cnt += 1
                else:
                    w_cnt += 1
            else:
                if board[x+i][y+j] == 'B':
                    b_cnt += 1
                else:
                    w_cnt += 1
    return min(w_cnt, b_cnt)

answer = 64
for i in range(N-7):
    for j in range(M-7):
        answer = min(answer, checkBoard(i,j))

print(answer)