import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    goal = "hello"
    j = 0
    for i in s:
        if j < len(goal) and i == goal[j]:
            j += 1
    if j == len(goal):
        print("YES")
    else:
        print("NO")
            

if __name__ == "__main__":
    solve()