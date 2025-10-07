import math

def solution(wallpaper):
    행길이 = len(wallpaper)
    열길이 = len(wallpaper[0])
    
    x = []
    y = []
    
    for r in range(행길이):
        for c in range(열길이):
            if wallpaper[r][c] == '#':
                x.append(r)
                y.append(c)
    
    
    answer = [min(x), min(y), max(x)+1, max(y)+1]
    return answer