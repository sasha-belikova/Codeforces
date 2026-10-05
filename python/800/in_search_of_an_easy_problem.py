import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    p = map(int, input().split())
    result = "EASY"
    for i in p:
        if i == 1:
            result = "HARD"
            break
    print(result)

    


if __name__ == "__main__":
    solve()