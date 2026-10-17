import sys
input = sys.stdin.readline

def solve():
    a = int(input())
    b = int(input())
    c = int(input())

    result = []

    result.append(a+b+c)
    result.append(a*b*c)
    result.append((a + b) * c)
    result.append(a * (b + c))
    
    print(max(result))
        
if __name__ == "__main__":
    solve()