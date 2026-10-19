import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    result = []

    for i in range(1, n+1):
        if i % 2 != 0:
            body = '#' * m
            result.append(body)
        elif i % 4 == 0:
            body = '#' + (m - 1)*'.'
            result.append(body)
        elif i % 2 == 0:
            body = (m - 1)*'.' + '#'
            result.append(body)

    for k in result:
        print(k) 
 
   
if __name__ == "__main__":
    solve()