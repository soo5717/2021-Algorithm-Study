def solution(m, musicinfos):
    correct_music_title = ''
    check_melody = change_melody(m)
    
    max_time = 0
    for music_info in musicinfos:
        music_info = music_info.split(',')
        time = calculate_time(music_info)
        melody = change_melody(music_info[3])
        new_melody = melody * (time // len(melody)) + melody[0:time % len(melody)]
        if check_melody in new_melody:
            if max_time < time:
                max_time = time
                correct_music_title = music_info[2]
    
    if correct_music_title == '':
        return "(None)"
    else:
        return correct_music_title

def change_melody(melody):
    melody = melody.replace('C#', 'H')
    melody = melody.replace('D#', 'I')
    melody = melody.replace('F#', 'J')
    melody = melody.replace('G#', 'K')
    melody = melody.replace('A#', 'L')
    return melody

def calculate_time(music_info):
    start = music_info[0]
    end = music_info[1]
    
    hour = int(end.split(':')[0]) - int(start.split(':')[0])
    minute = int(end.split(':')[1]) - int(start.split(':')[1])
    
    if hour == 0:
        return minute
    else:
        return 60 * hour + minute