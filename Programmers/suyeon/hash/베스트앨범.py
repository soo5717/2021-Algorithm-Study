def solution(genres, plays):
    genre_dict = {}
    play_dict = {}
    for i, genre_play in enumerate(zip(genres, plays)):
        genre, play = genre_play[0], genre_play[1]
        genre_dict[genre] = genre_dict.get(genre, 0) + play
        play_dict[genre] = play_dict.get(genre, []) + [(play, i)]
    
    genre_dict = dict(sorted(genre_dict.items(), key=lambda x: -x[1]))
    
    answer = []
    for genre in genre_dict:
        _, idx = zip(*sorted(play_dict.get(genre), key=lambda x: -x[0]))
        answer += idx[:2]
    return answer