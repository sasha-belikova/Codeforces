import sys
input = sys.stdin.readline

def solve():
    k, r = map(int, input().split())
    iteration = k
    count = 1
    if k % 10 == 0 or k % 10 == r:
        count = 1
    else:
        while True:
            count += 1
            k += iteration
            if k % 10 == 0 or k % 10 == r:
                break
    print(count)
        
        
if __name__ == "__main__":
    solve()