from collections import defaultdict

def solution(id_list, report, k):
    
    set_report = set(report)
    report_count = defaultdict(int)
    for r in set_report:
        유저id, 신고id = r.split()
        report_count[신고id] += 1
        
    정지id = [key for key,value in report_count.items() if value >= k]
    
    result = [0] * len(id_list)
    for r in set_report:
        유저id, 신고id = r.split()
        if 신고id in 정지id:
            result[id_list.index(유저id)] += 1
    return result