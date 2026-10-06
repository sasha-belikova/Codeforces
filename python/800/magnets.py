import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    pairs = []
    for _ in range(n):
        ij = int(input())
        pairs.append(ij)
    result = 1        # As we at least have one row
    for i in range(n-1):
        current = pairs[i]
        next = pairs[i + 1]
        if current != next:
            result +=1
    print(result)


    
            

if __name__ == "__main__":
    solve()