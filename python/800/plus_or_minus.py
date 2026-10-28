import sys
from bisect import bisect_left
input = sys.stdin.readline

def solve():
    t = int(input())
    result = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        if c > a:
            result.append("+")
        else:
            result.append("-")
    
    for i in result:
        print(i)
        
           
if __name__ == "__main__":
    solve()