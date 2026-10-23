import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    result = []
    for _ in range(t):
        s = input().strip()
        if s.upper() == "YES":
            result.append("YES")
        else:
            result.append("NO")

    for i in result:
        print(i)
    

if __name__ == "__main__":
    solve()