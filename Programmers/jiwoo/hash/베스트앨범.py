def solution(genres, plays):
    answer = []
    
    genre_count = {}
    for genre, play in zip(genres, plays):
        if genre in genre_count.keys():
            genre_count[genre] += play
        else:
            genre_count[genre] = play

    song_play_count = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        counts = genre_count[genre]
        if genre in song_play_count.keys():
            if len(song_play_count[genre]) >= 2:
                song_play_count[genre].append([counts, play, i])
                song_play_count[genre] = sorted(song_play_count[genre], key = lambda x: -x[1])[:2]
            else:
                song_play_count[genre].append([counts, play, i])
        else:
            song_play_count[genre] = [[counts, play, i]]

    song_play_values = sum(song_play_count.values(), [])
    song_play_sort = sorted(song_play_values, key=lambda x: (-x[0], -x[1], x[2]))

    return [i[2] for i in song_play_sort]