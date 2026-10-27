import sys
from bisect import bisect_right
input = sys.stdin.readline

def solve():
    n = int(input())                       # n - ampunt of shops
    x = list(map(int, input().split()))    # price of bottle in each shop
    q = int(input())                       # days to buy
    
    x.sort()
    result = []

    for _ in range(q):  
        m = int(input())                  # money on each day
        result.append(bisect_right(x, m))

    for j in result:
        print(j)


if __name__ == "__main__":
    solve()
