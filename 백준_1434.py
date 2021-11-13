N, M = map(int, input().split())
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))
box_space = 0
book_space = 0

for i in range(len(boxes)):
    box_space += boxes[i]

for _ in range(len(books)):
    book_space += books[_]

print(box_space - book_space)


