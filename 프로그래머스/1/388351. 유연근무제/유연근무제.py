def ttm(time):
    hours = time//100
    minutes = time%100
    
    return hours*60+minutes
    

def solution(schedules, timelogs, startday):
    
    answer = 0
    
    for 번호 in range(len(schedules)):
        day = startday
        event = 0
        for timelog in timelogs[번호]:
            if day >= 6 or ttm(schedules[번호]) + 10 >= ttm(timelog):
                event += 1
            day = day % 7 + 1
        if event == 7:
            answer += 1
    
    
    return answer