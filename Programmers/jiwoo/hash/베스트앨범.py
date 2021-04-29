def solution(genres, plays):
    answer = []
    
    genreCount = {}
    for genre, play in zip(genres, plays):
        if genre in genreCount.keys():
            genreCount[genre] += play
        else:
            genreCount[genre] = play

    songPlayCount = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        counts = genreCount[genre]
        if genre in songPlayCount.keys():
            if len(songPlayCount[genre]) >= 2:
                songPlayCount[genre].append([counts, play, i])
                songPlayCount[genre] = sorted(songPlayCount[genre], key = lambda x: -x[1])[:2]
            else:
                songPlayCount[genre].append([counts, play, i])
        else:
            songPlayCount[genre] = [[counts, play, i]]

    songPlayValues = sum(songPlayCount.values(), [])
    songPlaySort = sorted(songPlayValues, key=lambda x: (-x[0], -x[1], x[2]))

    return [i[2] for i in songPlaySort]