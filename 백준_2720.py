def fn(num):
    Q, D, N, P = 0, 0, 0, 0

    Q = num // 25
    num -= (25 * Q)

    D = num // 10
    num -= (10 *D)

    N = num // 5
    num -= (5 *N)

    P = num // 1

    print(Q, D, N, P)

T = int(input())

for i in range(T):
    num = int(input())
    fn(num)
