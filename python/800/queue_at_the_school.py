import sys
input = sys.stdin.readline

def solve():
    n, t = map(int, input().split())
    s = input().strip()
    s = list(s)
    for _ in range(t):
        i = 0
        while i < n - 1:
            current = s[i]
            next = s[i + 1]
            if current + next == "BG":
                s[i] = "G"
                s[i+1] = "B"
                i += 2
            else:
                i+=1
    s = ''.join(s)
    print(s)

    

if __name__ == "__main__":
    solve()