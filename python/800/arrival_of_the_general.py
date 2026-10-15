import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    m = min(a)
    min_place = len(a) - a[::-1].index(m)  # as we can accidentally take the first minimal number that is not best for us
    max_place = a.index(max(a)) + 1

    max_sec = max_place - 1
    min_sec = n - min_place

    if max_place > min_place:
        result = max_sec + min_sec - 1
        print(result)
    else:
        result = max_sec + min_sec
        print(result)



if __name__ == "__main__":
    solve()