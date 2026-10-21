import sys
input = sys.stdin.readline

def solve():
    x = list(map(int, input().split()))
    x = sorted(x)
    meeting_point = x[1]
    count = 0
    for i in x:
        remaining = abs(meeting_point - i)
        count += remaining

    print(count)


if __name__ == "__main__":
    solve()