import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for i in s if i.islower())

    if upper == len(s):
        print(s.swapcase())
    elif s[0] == s[0].lower() and lower == 1:
        print(s.swapcase())
    else:
        print(s)


if __name__ == "__main__":
    solve()