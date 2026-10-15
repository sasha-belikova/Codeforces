import sys
input = sys.stdin.readline

def solve():
    p = (input().strip())
    unique = list(set(p))
    result = "NO"
    for i in unique:
        if i in "H Q 9":
            result = "YES"
            break
    print(result)
         

if __name__ == "__main__":
    solve()