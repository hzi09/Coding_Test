def solution(todo_list, finished):
    id = list(filter(lambda x: finished[x] == False, range(len(finished))))
    return [todo_list[i] for i in id]