from collections import Counter

def solution(k, tangerine):
    크기별_개수 = Counter(tangerine)
    
    개수_내림차순 = sorted(크기별_개수.values(), reverse=True)
    
    상자에_담은_귤 = 0
    종류_개수 = 0
    
    for 개수 in 개수_내림차순:
        상자에_담은_귤 += 개수
        종류_개수 += 1
        
        if 상자에_담은_귤 >= k:
            break
            
    return 종류_개수