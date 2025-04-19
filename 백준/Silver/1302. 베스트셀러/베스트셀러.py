n = int(input())

books = [input() for _ in range(n)]
book_list = set(books)
book_cnt = []

for book in book_list :
    book_cnt.append([books.count(book), book])

book_cnt.sort(key=lambda x: (-x[0], x[1]))

print(book_cnt[0][1])
