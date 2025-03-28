def solution(survey, choices):
    scores = {
        "R": 0, "T": 0,
        "C": 0, "F": 0,
        "J": 0, "M": 0,
        "A": 0, "N": 0
    }

    for i in range(len(survey)):
        s = survey[i]
        choice = choices[i]

        if choice < 4:
            scores[s[0]] += 4 - choice
        elif choice > 4:
            scores[s[1]] += choice - 4

    result = ""
    indicators = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]

    for a, b in indicators:
        if scores[a] >= scores[b]:
            result += a
        else:
            result += b

    return result
