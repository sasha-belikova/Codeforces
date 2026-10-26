import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    result = []
    for _ in range(t):                       
        n, k = map(int, input().split())        # n - amount of elements
                                                # k - max elements to turn
        a = list(map(int, input().split()))     # elements
        sor = sorted(a)

        if k == 1 and sor != a:
            result.append("NO")
        else:
            result.append("YES")

    for i in result:
        print(i)
    
        
if __name__ == "__main__":
    solve()