import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    result = []
    for _ in range(t):
        r = int(input())

        if r <= 1399:
            result.append("Division 4")
        elif r <= 1599:
            result.append("Division 3")
        elif r <= 1899:
            result.append("Division 2")
        elif r >= 1900:
            result.append("Division 1")

    for i in result:
        print(i)

    
               

if __name__ == "__main__":
    solve()