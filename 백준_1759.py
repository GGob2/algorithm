from itertools import combinations
import sys

input = sys.stdin.readline

vowels = ('a', 'e', 'i', 'o', 'u')

l, c = map(int, input().split())

char_list = list(input().split())
char_list.sort()

for char in combinations(char_list, l):
    count = 0
    for i in char:
        if i in vowels:    
            count+= 1
    if count >= 1 and count <= l-2:
        print("".join(char))

