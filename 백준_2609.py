a, b = map(int, input().split())

def common_factor(n, t):
    while (n != t):
        if (n>t):
            n -= t
        else:
            t -= n
    return n

print(common_factor(a, b))
print((a*b) // common_factor(a, b))
