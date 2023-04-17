import sys
from itertools import permutations          # 순열 생성

input = sys.stdin.readline

n, m = map(int, input().split())

result = permutations(range(1, n+1), m)     # 1 ~ n 까지의 범위에서 
                                            # m개의 가능한 모든 수열 추출
for i in result:
    print(" ".join(map(str, i)))            


