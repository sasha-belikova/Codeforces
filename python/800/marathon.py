import sys
from bisect import bisect_left
input = sys.stdin.readline

def solve():
    t = int(input())
    result = []
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        list_ = [b, c, d]
        list_.sort()

        result.append(bisect_left(list_, a))

    for i in result:
        print(3 - i)

             
if __name__ == "__main__":
    solve()