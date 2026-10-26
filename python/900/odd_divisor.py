import sys
input = sys.stdin.readline


def solve():
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        if n % 2 == 0:
            binary_n = str(bin(n))
            if binary_n.count('1') == 1:
                result.append("NO")
            else:
                result.append("YES")
        else:
            result.append("YES")

    for i in result:
        print(i)



    
if __name__ == "__main__":
    solve()