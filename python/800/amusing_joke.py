import sys
input = sys.stdin.readline

def solve():
    a = input().strip()
    b = input().strip()
    s = input().strip()

    together = a + b

    if sorted(s) == sorted(together):
        print("YES")
    else:
        print("NO")
    

if __name__ == "__main__":
    solve()