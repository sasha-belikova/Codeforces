import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    while True:
        n += 1
        k = list(map(int, str(n)))
        if len(k) == len(set(k)):
            print(n)
            break


if __name__ == "__main__":
    solve()