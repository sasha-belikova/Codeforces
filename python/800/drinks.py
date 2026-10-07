import sys
input = sys.stdin.readline

def solve():
    n = float(input())
    p = map(int, input().split())
    p = list(p)
    orange_procent = float(sum(p))
    result = round(orange_procent / n, 12)
    print(result)

if __name__ == "__main__":
    solve()