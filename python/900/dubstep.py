
import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    no_wub = s.replace("WUB", " ")
    result = " ".join(no_wub.split())
    print(result)


if __name__ == "__main__":
    solve()
