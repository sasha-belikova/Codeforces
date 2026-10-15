import sys
input = sys.stdin.readline



def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    result = " ".join(map(str, a))
    print(result)
         

if __name__ == "__main__":
    solve()