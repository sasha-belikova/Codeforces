import sys
input = sys.stdin.readline

def solve():
    s, n = map(int, input().split())
    result = "YES"
    x = []
    y = []
    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    pairs = list(zip(x, y))
    pairs = sorted(pairs)

    for i, j in pairs:
        if s > i:
            s += j
        else:
            result = "NO"
            break

    if result == "NO":
        print(result)
    else:
        print(result)
    


if __name__ == "__main__":
    solve()