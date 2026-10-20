import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    t = list(map(int, input().split()))
    count_even = len([i for i in t if i % 2 == 0])

    if count_even >= 2:
        for k in range(n):
            if t[k] % 2 != 0:
                print(k+1)
    else:
        for k in range(n):
            if t[k] % 2 == 0:
                print(k+1)


if __name__ == "__main__":
    solve()