import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    passengers = []
    count = 0
    for i, j in zip(a, b):
        count = count - i + j
        passengers.append(count)
    print(max(passengers))



    


if __name__ == "__main__":
    solve()