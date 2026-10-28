import sys
input = sys.stdin.readline

def solve():
    x = list(map(int, input().split()))
    x.sort()
    if len(set(x)) == 2:
        result = int(x[0] // 2)
        print(result, result, result)
    else:
        a = x[0] + x[1] - x[3]
        b = x[0] - a
        c = x[1] - a
        print(a, b, c)
      
        
if __name__ == "__main__":
    solve()