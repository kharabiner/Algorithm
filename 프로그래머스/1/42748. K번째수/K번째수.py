def solution(array, commands):
    answer = []
    
    for command in commands:
        자른배열 = array[command[0]-1:command[1]]
        정렬 = sorted(자른배열)
        answer.append(정렬[command[2]-1])
    
    return answer