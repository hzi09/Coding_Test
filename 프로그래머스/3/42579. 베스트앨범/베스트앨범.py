def solution(genres, plays):
    genre_play_cnt = {}
    song_list = {}
    
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if genre not in genre_play_cnt:
            genre_play_cnt[genre] = 0
            song_list[genre] = []
        genre_play_cnt[genre] += play
        song_list[genre].append((i, play))
        
    for genre in song_list :
        song_list[genre].sort(key=lambda x: (-x[1], x[0]))
        
    sorted_genres = sorted(genre_play_cnt.keys(), key=lambda x: -genre_play_cnt[x])
                           
    result = []
    for genre in sorted_genres :
        result.extend([song[0] for song in song_list[genre][:2]])
    return result