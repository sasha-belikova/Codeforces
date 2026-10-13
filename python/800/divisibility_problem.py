import sys
input = sys.stdin.readline


def solve():
    t = int(input())

    for _ in range(t):
        i, j = map(int, input().split())
        print((j - i % j) % j)

            
if __name__ == "__main__":
    solve()