import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    t = list(map(int, input().split()))
    police = 0
    result = 0

    for i in t:
        if i > 0:
            police += i
        elif i < 0 and police >= 1:
            police -= 1
        elif i < 0 and police < 1:
            result += 1

    print(result)
        

    
        
if __name__ == "__main__":
    solve()