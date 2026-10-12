import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    if n % 2 == 0:
        half = n / 2
    else: 
        half = n // 2 + 1

    if k <= half:
        result = k + k - 1
    else:
        result = (k - half) * 2

    print(int(result))

if __name__ == "__main__":
    solve()