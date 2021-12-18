n = int(input())

crane = list(map(int, input().split()))

box = int(input())

box_weight = list(map(int, input().split()))


crane.sort(reverse=True)
box_weight.sort(reverse=True)

result = 0
move = [0 for _ in range(box)]
cnt = 0
posi = [0] * n





