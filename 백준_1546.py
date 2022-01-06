n = int(input())
score_list = list(map(int, input().split()))

m = max(score_list)
score = []
for i in range(n):
    if score_list[i] == m:
        score.append(100)
    else:
        score.append(((score_list[i] / m) * 100))

print(sum(score) / len(score))