def solution(name, yearning, photo):
    answer = []
    
    for current_photo in photo:
        sum = 0
        for i in range(len(name)):
            if name[i] in current_photo:
                sum += yearning[i]
        answer.append(sum)
    
    return answer