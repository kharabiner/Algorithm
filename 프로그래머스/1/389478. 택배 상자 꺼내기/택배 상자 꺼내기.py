def solution(총, 한줄, num):
    층수 = ((num-1) // 한줄) + 1
    나머지 = num % 한줄
    if 나머지 == 0:
        나머지 = 한줄
    target = 0
    if 층수 % 2 == 0: #짝수층일때
        target = 한줄*2 - (2*나머지-1)
        
    else:
        target = 한줄*2 - (2*나머지-1)
    print(target)
    cnt = 1
    while True:
        if num + target <= 총:
            cnt += 1
            num += target
            target = 한줄*2 - target
            
        else:
            break
    
    # 10 9 8 7 6
    # 1 2 3 4 5
    
    # 1 3 5 7 9 11
    # 11 9 7 5 3 1
    # (num*2)- (2n-1)
    answer = cnt
    return answer