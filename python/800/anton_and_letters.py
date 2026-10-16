import sys
input = sys.stdin.readline

def solve():
    s = input().strip()      # there are always minimum one { and one }. So its two together
    s_at_all = list(set(s))
    count = 0
    for i in s_at_all:
        if i in "  ,":
            count +=1
    result = len(s_at_all) - count - 2  
    print(result)


    


if __name__ == "__main__":
    solve()