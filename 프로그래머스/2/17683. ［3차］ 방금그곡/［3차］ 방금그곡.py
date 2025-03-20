def solution(m, musicinfos):
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f")\
         .replace("G#", "g").replace("A#", "a").replace("B#", "b")

    answer = ("(None)", 0)

    for music in musicinfos:
        music = music.split(',')
        h1, m1 = map(int, music[0].split(':'))
        h2, m2 = map(int, music[1].split(':'))
        play_time = (h2 * 60 + m2) - (h1 * 60 + m1)

        title = music[2]
        melody = music[3]

        melody = melody.replace("C#", "c").replace("D#", "d").replace("F#", "f")\
                       .replace("G#", "g").replace("A#", "a").replace("B#", "b")

        full_melody = (melody * (play_time // len(melody) + 1))[:play_time]

        if m in full_melody:
            if play_time > answer[1]:
                answer = (title, play_time)

    return answer[0]
