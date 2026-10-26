import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    k = list(map(int, input().split()))

    if n >= 2:
        max_ = max(k[0], k[1])
        min_ = min(k[0], k[1])
        if max_ != min_:
            count = 1
        else:
            count = 0

        for i in range(2, n):
            if k[i] > max_:
                max_ = k[i]
                count += 1
            elif k[i] < min_:
                min_ = k[i]
                count += 1
        print(count)
    else:
        print(0)


if __name__ == "__main__":
    solve()