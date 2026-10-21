import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    Vanya = "First"
    Vova = "Second"
    result = []
    for _ in range(t):
        n = int(input())
        if (n - 1) % 3 == 0:
            result.append(Vanya)
        elif (n + 1) % 3 == 0:
            result.append(Vanya)
        else:
            result.append(Vova)

    for i in result:
        print(i)


if __name__ == "__main__":
    solve()