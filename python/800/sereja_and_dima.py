import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    k = list(map(int, input().split()))

    result = []
    left = 0
    right = len(k) - 1

    while left <= right:
        if k[left] >= k[right]:
            result.append(k[left])
            left += 1   
        else:
            result.append(k[right])
            right -= 1

    sergei = 0
    dima = 0

    for i in range(n):
        if i % 2 == 0 or i == 0:
            sergei += result[i]
        else:
            dima += result [i]

    print(sergei, dima)
               

if __name__ == "__main__":
    solve()