def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    # ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
    # ext를 인덱스로
    if ext == 'code':
        index = 0
    elif ext == 'date':
        index = 1
    elif ext == 'maximum':
        index = 2
    else:
        index = 3
    
    # 추출
    ext_list = []
    for i in data:
        if i[index] < val_ext:
            ext_list.append(i)
    
    # sort_by를 인덱스로
    if sort_by == 'code':
        index = 0
    elif sort_by == 'date':
        index = 1
    elif sort_by == 'maximum':
        index = 2
    else:
        index = 3
        
    # 정렬
    answer = sorted(ext_list, key=lambda x: x[index])
    
    
    
    return answer