def solution(new_id):
    # 1
    lower =  new_id.lower()
    # 2
    allowed_chars = set('0123456789abcdefghijklmnopqrstuvwxyz-_.')
    remove = ''.join([char for char in lower if char in allowed_chars])
    # 3
    while '..' in remove:
        remove = remove.replace('..', '.')
    remove = list(remove)
    # 4
    if remove and remove[0] == '.':
        remove.pop(0)
    if remove and remove[-1] == '.':
        remove.pop(-1)
    
    # 5
    if not remove:
        remove = ['a']
    # 6
    sliced = remove[0:15]
    
    #7
    if len(sliced) <= 2:
        while not len(sliced) == 3:
            sliced.append(sliced[-1])
    if sliced and sliced[-1] == '.':
        sliced.pop(-1)
        
    answer = ''.join(sliced)
    return answer