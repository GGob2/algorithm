n = int(input())
book = {}
for i in range(n):
    book_subject = input()
    
    if book_subject in book:
        book[book_subject] += 1
    else:
        book[book_subject] = 1

high_freq = max(book.values())
result = []

for key, value in book.items():
    if high_freq == value:
        result.append(key)

print(sorted(result)[0])


