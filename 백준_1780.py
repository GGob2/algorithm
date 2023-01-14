import sys
input = sys.stdin.readline

n = int(input())

num_list = []

for i in range(n):
    num = input().split()
    num_list.append(num)

def check_paper(list):
    for _ in range(0, n, n/3):
        


