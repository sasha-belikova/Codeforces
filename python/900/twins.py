import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    half = sum(a)/2
    count = 0 
    result = 0
    for i in a:
        count += i
        result += 1
        if count > half:
            break
    print(result)


if __name__ == "__main__":
    solve()