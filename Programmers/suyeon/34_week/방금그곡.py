def convert_time(start, end):
    start_h, start_m = start.split(':')
    end_h, end_m = end.split(':')
    
    return (int(end_h) * 60 + int(end_m)) - (int(start_h) * 60 + int(start_m))

def convert_score(score):
    return score.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def solution(m, musicinfos):
    answer = []
    m = convert_score(m)
    
    for info in musicinfos:
        start_time, end_time, title, score = info.split(',')
        
        play_time = convert_time(start_time, end_time)
        score = convert_score(score)
        
        score = score * (play_time // len(score) + 1)
        score = score[:play_time]
        
        for i in range(len(score)):
            if m == score[i:i + len(m)]:
                answer.append((play_time, title))
                break
                
    return '(None)' if not answer else sorted(answer, key=lambda x:-x[0])[0][1]