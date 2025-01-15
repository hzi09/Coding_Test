def solution(phone_number):
    hide = phone_number[:-4]
    return phone_number.replace(hide, '*' * len(hide))