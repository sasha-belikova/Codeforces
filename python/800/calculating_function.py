import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    if n % 2 == 0:
        result = n // 2
    else:
        result = - (n // 2 + 1)
    print(result)
        
if __name__ == "__main__":
    solve()