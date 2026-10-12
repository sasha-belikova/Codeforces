import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    p = map(int, input().split())
    p = list(p)
    k = []
    for i in range(1, n+1):
        for j in p:
            if i == j:
                number = p.index(j)
                k.append(number + 1)
    result = " ".join(map(str, k))
    print(result)


if __name__ == "__main__":
    solve()