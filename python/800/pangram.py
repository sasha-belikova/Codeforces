import sys
input = sys.stdin.readline

# we have 26 letters in latin alphabet

def solve():
    n = int(input())
    s = input().strip()

    if n < 26:
        print("NO")
    else:
        s = s.lower()
        s_list = list(s)
        unique_num = len(set(s_list))

        if unique_num == 26:
            print("YES")
        else:
            print("NO")
    

if __name__ == "__main__":
    solve()