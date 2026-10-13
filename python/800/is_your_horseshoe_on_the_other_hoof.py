import sys
input = sys.stdin.readline

def solve():
    s = list(map(int, input().split()))
    whole_s = len(s)
    unique_s = len(list(set(s)))
    result = whole_s - unique_s
    print(result)


if __name__ == "__main__":
    solve()