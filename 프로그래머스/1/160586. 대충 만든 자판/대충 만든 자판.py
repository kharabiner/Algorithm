def solution(keymap, targets):
    answer = []
    
    # A-Z 딕셔너리 만들기
    min_dict = {chr(x):float('inf') for x in range(65, 91)}
    # keymap 순회하며 최저값 저장
    for 문자열 in keymap:
        for index in range(len(문자열)):
            if min_dict[문자열[index]] > index + 1:
                min_dict[문자열[index]] = index + 1
    # targets 순회하며 값 합산
    for 문자열 in targets:
        sum = 0
        for 문자 in 문자열:
            if min_dict[문자] == float('inf'):
                sum = -1
                break
            sum += min_dict[문자]
        answer.append(sum)
    
    return answer