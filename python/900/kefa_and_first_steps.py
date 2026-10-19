import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    result = []
    count = 0

    for i in range(n-1):
        current = a[i]
        next = a[i+1]
        if current <= next:
            count += 1
        else:
            result.append(count)
            count = 0
    result.append(count)
    
    print(max(result) + 1)
    
        



    
 
   
if __name__ == "__main__":
    solve()