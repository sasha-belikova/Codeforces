import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    result = []
    for _ in range(t):
        count = 0
        pre_result = []
        n = str(input().strip())
        for i in reversed(range(len(n))):
            if n[i] != '0':
                count += 1
                null_num = len(n) - 1 - i
                fin_number = str(n[i]) + '0'*null_num
                pre_result.append(fin_number)
        result.append(count)
        result.append(pre_result)

    for i in result:
        if isinstance(i, (list, tuple)):
            print(' '.join(map(str, i)))
        else:
            print(i)


if __name__ == "__main__":
    solve()