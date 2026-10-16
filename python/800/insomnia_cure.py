import sys
input = sys.stdin.readline

def solve():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())

    d = int(input())   # dragons at all

    count = 0
    if n == 1 or l == 1 or k ==1 or m == 1:
        print(d)
    else:
        for i in range(1, d+1):
            if i % n != 0 and i % k != 0 and i % l != 0 and i % m != 0: 
                count += 1
        print(d - count)
        


if __name__ == "__main__":
    solve()