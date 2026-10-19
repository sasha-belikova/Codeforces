import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        if n <= 2:
            result.append(0)
        else:
            if n % 2 == 0:
                result.append(n//2 - 1)
            else:
                result.append(n // 2)

    for i in result:
        print(i)

        
if __name__ == "__main__":
    solve()