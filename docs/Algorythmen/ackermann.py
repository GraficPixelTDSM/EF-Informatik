# Werte:
import sys

sys.setrecursionlimit(10**9)


def ack(m, n):
    if m == 0:
        ans = n + 1
    elif n == 0:
        ans = ack(m - 1, 1)
    else:
        ans = ack(m - 1, ack(m, n - 1))
    return ans


for i in range(6):
    for j in range(6):
        print(ack(i, j))
