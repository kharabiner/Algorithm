from collections import defaultdict
from itertools import combinations

def solution(friends, gifts):
    
    준선물수 = defaultdict(int)
    받은선물수 = defaultdict(int)
    주고받은수 = defaultdict(int)
    
    for gift in gifts:
        주고받은수[gift] += 1
        
        준사람, 받은사람=gift.split()
        준선물수[준사람] += 1
        받은선물수[받은사람] += 1
    
    받을선물 = defaultdict(int)
    # 두사람 사이 주고받은 기록 있으면? 두 사람 사이에 더많은 선물 준 사람 하나 받음
    for friend1, friend2 in combinations(friends, 2):
        if friend1 == friend2: continue
        give12 = 주고받은수.get(' '.join([friend1, friend2]), 0)
        give21 = 주고받은수.get(' '.join([friend2, friend1]), 0)
        if give12 > give21:
            받을선물[friend1] += 1
        elif give12 < give21:
            받을선물[friend2] += 1
        else:
            # 없거나 같으면? 선물지수 더 큰 사람이 작은 사람에게 하나 받음
            # 선물지수 = 준선물-받은선물
            print('##########',준선물수[friend1]-받은선물수[friend1], 준선물수[friend2]-받은선물수[friend2])
            if 준선물수[friend1]-받은선물수[friend1] > 준선물수[friend2]-받은선물수[friend2]:
                받을선물[friend1] += 1
            elif 준선물수[friend1]-받은선물수[friend1] < 준선물수[friend2]-받은선물수[friend2]:
                받을선물[friend2] += 1
    # 가장 많이 받을 선물의 수
    answer =  max(받을선물.values(), default=0)
    return answer