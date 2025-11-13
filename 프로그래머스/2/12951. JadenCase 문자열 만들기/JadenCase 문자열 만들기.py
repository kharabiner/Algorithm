def solution(s):
    answer = ''
    
    소문자 = list(s.lower())
    
    이전 = ' '
    for 인덱스, 문자 in enumerate(소문자):
        if 이전 == ' ' and 문자.islower():
            소문자[인덱스] = 소문자[인덱스].upper()
        이전 = 문자
    
    answer = ''.join(소문자)
    
    return answer