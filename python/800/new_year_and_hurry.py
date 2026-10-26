import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    pure_time = 240 - k
    count = 0
    not_all = False
    for i in range(1, n+1):
        task_time = 0
        task_time = 5 * i
        count += task_time

        if pure_time < count:
            not_all = True
            print(i - 1)
            break

    if not_all != True:
        print(n)

if __name__ == "__main__":
    solve()