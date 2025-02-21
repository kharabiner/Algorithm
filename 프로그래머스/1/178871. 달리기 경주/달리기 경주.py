def solution(players, callings):
    
    플레이어등수 = {players[i]:i+1 for i in range(len(players))}
    등수플레이어 = {i+1:players[i] for i in range(len(players))}
    
    for calling in callings:
        등수 = 플레이어등수[calling] # 4등
        등수플레이어[등수], 등수플레이어[등수-1] = 등수플레이어[등수-1], 등수플레이어[등수]
        플레이어등수[등수플레이어[등수]], 플레이어등수[등수플레이어[등수-1]] = 플레이어등수[등수플레이어[등수-1]], 플레이어등수[등수플레이어[등수]]
        
    answer = [x for x in 등수플레이어.values()]
    
    return answer

