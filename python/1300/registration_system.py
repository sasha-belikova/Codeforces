import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    users = set()
    count = {}
    result = []

    for _ in range(n):
        s = input().strip()
        if s not in users:
            result.append("OK")
            users.add(s)
            count[s] = 1
        else:
            i = count.get(s, 1)
            while s + str(i) in users:
                i += 1
            new_name = s + str(i)
            result.append(new_name)
            users.add(new_name)
            count[s] = i + 1

    for i in result:
        print(i)
    
        
if __name__ == "__main__":
    solve()
