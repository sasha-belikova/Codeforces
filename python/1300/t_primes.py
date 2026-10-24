import sys
import math as mt
input = sys.stdin.readline

def solve():
    n = int(input())
    m = list(map(int, input().split()))

    limit = 10**6
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    for i in m:
        root = mt.isqrt(i)
        if root**2 == i and is_prime[root]:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()