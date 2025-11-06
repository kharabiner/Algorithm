def solution(n, lost, reserve):
    
    도난 = set(lost) - set(reserve)
    여벌 = set(reserve) - set(lost)

    for 학생 in sorted(도난):
        if 학생-1 in 여벌:
            도난.remove(학생)
            여벌.remove(학생-1)
        elif 학생+1 in 여벌:
            도난.remove(학생)
            여벌.remove(학생+1)
    
    return n-len(도난)