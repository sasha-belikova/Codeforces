import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    p = []
    q = []
    for _ in range(n):
        x,y = map(int, input().split())
        p.append(x)
        q.append(y)

    pairs = list(zip(p,q))
    count = 0

    for i, j in pairs:
        if j - i >= 2:
            count += 1

    print(count)
            

    

if __name__ == "__main__":
    solve()