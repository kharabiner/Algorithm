import math

def solution(wallpaper):
    행길이 = len(wallpaper)
    열길이 = len(wallpaper[0])
    
    lux = math.inf
    luy = math.inf
    rdx = 0
    rdy = 0
    
    for r in range(행길이):
        for c in range(열길이):
            if wallpaper[r][c] == '#':
                lux = min(lux, r)
                luy = min(luy, c)
                rdx = max(rdx, r)
                rdy = max(rdy, c)
    
    
    answer = [lux, luy, rdx+1, rdy+1]
    return answer