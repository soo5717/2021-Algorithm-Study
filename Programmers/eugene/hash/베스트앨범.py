def solution(genres, plays):
    answer = []
    
    category = set(genres)
    genre_plays = dict(zip(category, [0]*len(category)))

    for i in range(len(genres)):
        genre_plays[genres[i]] += plays[i]

    genre_sort = sorted(genre_plays.items(), key=lambda x:x[1], reverse=True)
    
    for genre in genre_sort:
        temp=[]
        for i in range(0, len(genres)):
            if genres[i] == genre[0]:
                temp.append((i, plays[i]))

        song_sort = list(map(lambda x:x[0],sorted(temp, key=lambda x:x[1], reverse=True)))
        answer += song_sort[:2]
        
    return answer