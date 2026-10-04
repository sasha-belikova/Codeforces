import sys
input = sys.stdin.readline

def solve():
    n, h = map(int, input().split())
    a = map(int, input().split())
    count = 0
    for i in a:
        if i <= h:
            count += 1
        else:
            count += 2
    print(count)
    


if __name__ == "__main__":
    solve()