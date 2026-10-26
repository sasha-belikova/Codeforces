import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    f = list(map(int, input().split()))
    f.sort()
    result = []

    for i in range(0, m - n + 1):
        needed = f[i:i + n]
        var = max(needed) - min(needed)
        result.append(var)

    print(min(result))

if __name__ == "__main__":
    solve()
