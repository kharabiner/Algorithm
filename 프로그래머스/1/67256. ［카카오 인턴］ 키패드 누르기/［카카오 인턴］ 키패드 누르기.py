
    

def solution(numbers, hand):
    좌표 = {1:(0,0), 2:(0,1), 3:(0,2),
          4:(1,0), 5:(1,1), 6:(1,2),
         7:(2,0), 8:(2,1), 9:(2,2),
         '*':(3,0), 0:(3,1), '#':(3,2)}
    
    left = '*'
    right = '#'
    save = []
    for number in numbers:
        if number in (2,5,8,0):
            distance_L = abs(좌표[number][0] - 좌표[left][0]) + abs(좌표[number][1] - 좌표[left][1])
            distance_R = abs(좌표[number][0] - 좌표[right][0]) + abs(좌표[number][1] - 좌표[right][1])
            print(distance_L, distance_R)
            if distance_L < distance_R:
                save.append('L')
                left = number
            elif distance_L > distance_R:
                save.append('R')
                right = number
            else:
                if hand == 'left':
                    save.append('L')
                    left = number
                else:
                    save.append('R')
                    right = number
        elif number in (1, 4, 7):
            save.append('L')
            left = number
        else:
            save.append('R')
            right = number
            
    answer = ''.join(save)
    return answer