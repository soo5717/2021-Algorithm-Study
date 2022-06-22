import datetime

def solution(m, musicinfos):
    play_times = dict()
    

    #Step1. m 재구성
    now_song_code = melody_find(m)
    #Step2. 곡 찾기
    for musicinfo in musicinfos:
        start, end, name, code = musicinfo.split(',')
        play_times[name]=0;
        # 시간 계산
        time = time_converter(start, end)
        
        # code 재구성
        song_code = melody_find(code)
        #네오가 기억한 멜로디(now_song_code)가 time분 안에 music(song_code)과 일치하는 시간 계산 = play_time
        total_song = song_code * (time //len(song_code)) + song_code[:time %len(song_code)]
        for i in range(len(total_song)):
            if (total_song[i:i+len(now_song_code)] == now_song_code):
                play_times[name] += len(now_song_code)
    # Step3. play_times에서 가장 긴 시간 -> 먼저 입력된 -> None 순서로 결과 RETURN
    # print(play_times)
    sorted_dict = sorted(play_times.items(),  key = lambda item: item[1],reverse=True)
    if sorted_dict[0][1] == 0:
        return "(None)"
    
    return sorted_dict[0][0]


def time_converter(start, end):
    time = datetime.datetime.strptime(end, "%H:%M") - datetime.datetime.strptime(start, "%H:%M") 
    return time.seconds//60


def melody_find(m):
    melody = []
    
    for i in range(len(m)):
        if i == len(m) - 1:
            if m[i] != '#':
                melody.append(m[i])
            break
        
        if m[i] == '#':
            continue
            
        if m[i+1] != '#':
            melody.append(m[i])
        else:
            melody.append(m[i]+m[i+1])
            
    return melody
