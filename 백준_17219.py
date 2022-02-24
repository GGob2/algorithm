import sys
input = sys.stdin.readline

n, m = map(int, input().split())

notepad = {}

for i in range(n):
    site, pw = input().split()
    notepad[site] = pw

for j in range(m):
    question_site = input().rstrip()
    print(notepad[question_site])