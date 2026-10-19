import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    result = []

    for _ in range(t):
        a, b, c = map(int, input().split())

        if a + b == c or a + c == b or b + c == a:
            result.append("YES")
        else:
            result.append("NO")

    for i in result:
        print(i)

     
if __name__ == "__main__":
    solve()