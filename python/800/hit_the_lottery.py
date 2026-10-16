import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    count = 0
    while True:
        if n >= 100:
            n = n - 100
            count += 1
        elif n >= 20:
            n = n - 20
            count += 1
        elif n >= 10:
            n = n - 10
            count += 1
        elif n >= 5:
            n = n - 5
            count += 1
        elif n >= 1:
            n = n - 1
            count += 1
        elif n == 0:
            break

    print(count)

    
        


if __name__ == "__main__":
    solve()