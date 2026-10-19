
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = list(map(int, input().split()))

    count = s.count(4)
    threes = s.count(3)
    twos = s.count(2)
    ones = s.count(1)

    count += threes
    ones = max(0, ones - threes)

    count += twos // 2
    if twos % 2:
        count += 1
        ones = max(0, ones - 2)

    count += (ones + 3) // 4

    print(count)

if __name__ == "__main__":
    solve()
