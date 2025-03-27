import re

def solution(today, terms, privacies):
    term_dict = {t[0]: int(t.split()[1]) for t in terms}

    def date_to_days(date_str):
        y, m, d = map(int, date_str.split('.'))
        return y * 12 * 28 + m * 28 + d

    today_days = date_to_days(today)
    answer = []

    for idx, entry in enumerate(privacies):
        date_str, term_type = entry.split()
        term_month = term_dict[term_type]

        y, m, d = map(int, date_str.split('.'))
        m += term_month
        y += (m - 1) // 12
        m = (m - 1) % 12 + 1

        expire_days = y * 12 * 28 + m * 28 + d - 1

        if expire_days < today_days:
            answer.append(idx + 1)

    return answer
