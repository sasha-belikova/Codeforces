import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = []
    b = []
    count = 0
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    for i in a:
        for j in b:
            if i == j:
                count += 1
    print(count)


if __name__ == "__main__":
    solve()