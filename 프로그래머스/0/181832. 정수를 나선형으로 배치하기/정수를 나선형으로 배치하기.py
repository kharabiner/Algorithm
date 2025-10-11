from collections import deque

def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    r = c = 0
    이동 = deque([[0,1], [1,0], [0,-1], [-1,0]])
    
    for number in range(1, n*n+1):
        answer[r][c] = number
        
        다음 = [r+이동[0][0], c+이동[0][1]]
        if 다음[0] > n-1 or 다음[0] < 0 or 다음[1] > n-1 or 다음[1] < 0 or answer[다음[0]][다음[1]] != 0:
            이동.rotate(-1)
        
        r += 이동[0][0]
        c += 이동[0][1]
        
    return answer