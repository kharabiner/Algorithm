from collections import deque

def solution(다리길이, 견디는무게, 트럭무게):
    경과시간 = 0
    다리위현재무게 = 0
    다리위 = deque()
    대기트럭 = deque(트럭무게)
    while True:
        경과시간 += 1
        # 제거
        for i in range(len(다리위)):
            트럭 = 다리위.popleft()
            트럭[1] -= 1
            if 트럭[1] > 0:
                다리위.append(트럭)
            else:
                다리위현재무게 -= 트럭[0]
        # 추가
        if 대기트럭 and 대기트럭[0] + 다리위현재무게 <= 견디는무게:
            트럭 = 대기트럭.popleft()
            다리위.append([트럭, 다리길이])
            다리위현재무게 += 트럭
        # 확인
        if not 다리위:
            break
        
    
    answer = 경과시간
    return answer