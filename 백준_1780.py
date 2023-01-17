# <https://www.acmicpc.net/problem/1780>

import sys
input = sys.stdin.readline

n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]

zero_paper = 0
one_paper = 0
minus_one_paper = 0

def dfs(r, c, n):
    global zero_paper, one_paper, minus_one_paper

    num = num_list[r][c]
    
    for i in range(r, r+n):
        for j in range(c, c+n):
            if num_list[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        dfs(r+k*n // 3, c+l*n // 3, n // 3)
                return


    if num == 0:
        zero_paper += 1
    elif num == 1:
        one_paper += 1
    else:
        minus_one_paper += 1

dfs(0,0,n)
print(minus_one_paper)
print(zero_paper)
print(one_paper)