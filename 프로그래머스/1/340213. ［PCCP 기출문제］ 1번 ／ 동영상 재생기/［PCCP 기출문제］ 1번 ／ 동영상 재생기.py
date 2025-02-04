from datetime import datetime, timedelta

def solution(video_len, pos, op_start, op_end, commands):
    video_len_time = datetime.strptime(video_len, '%M:%S')
    op_start_time = datetime.strptime(op_start, '%M:%S')
    op_end_time = datetime.strptime(op_end, '%M:%S')
    current = datetime.strptime(pos, '%M:%S')
    video_start_time = datetime.strptime('00:00', "%M:%S")
    
    if current >= op_start_time and current <= op_end_time:
        current = op_end_time
    
    for command in commands:
        if command == 'next':
            current = current + timedelta(seconds=10)
            if current > video_len_time:
                current = video_len_time
            if current >= op_start_time and current <= op_end_time:
                current = op_end_time
        else:
            current = current - timedelta(seconds=10)
            if current < video_start_time:
                current = video_start_time
            if current >= op_start_time and current <= op_end_time:
                current = op_end_time
    
    answer = current.strftime("%M:%S")
    
    return answer