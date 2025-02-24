from collections import deque
def solution(ingredient):
    햄버거 = deque(ingredient)
    판단큐 = deque()
    
    cnt = 0
    for i in range(len(햄버거)):
        if len(판단큐) < 3:
            판단큐.append(햄버거.popleft())
        else:
            판단큐.append(햄버거.popleft())
            if 판단큐[-1-3]==1 and 판단큐[-1-2]==2 and 판단큐[-1-1]==3 and 판단큐[-1]==1:
                cnt += 1
                판단큐.pop()
                판단큐.pop()
                판단큐.pop()
                판단큐.pop()
        
    return cnt