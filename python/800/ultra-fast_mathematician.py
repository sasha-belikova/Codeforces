import sys
input = sys.stdin.readline


def solve():
    n = input().strip()
    k = input().strip()
    result = []
    for i, j in list(zip(n, k)):
        if i != j:
            result.append(1)
        else:
            result.append(0)
    result = "".join(map(str, result))
    print(result)


if __name__ == "__main__":
    solve()