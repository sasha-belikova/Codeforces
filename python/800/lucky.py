import sys
input = sys.stdin.readline

def solve():
    t= int(input())
    result = []
    for _ in range(t):
        n = list(map(int, input().strip()))
        if sum(n[:3]) == sum(n[3:]):
            result.append("YES")
        else:
            result.append("NO")

    for i in result:
        print(i)
        
        
if __name__ == "__main__":
    solve()