import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    num_p_lvl = p[:1]
    num_q_lvl = q[:1]
    at_all = sum(num_p_lvl + num_q_lvl)

    if n > at_all:
        print("Oh, my keyboard!")
    else:
        lvl_row_p = p[1:]
        lvl_row_q = q[1:]
        at_all_row = list(set(lvl_row_p + lvl_row_q))

        if len(at_all_row) == n:
            print("I become the guy.")
        else:
            print("Oh, my keyboard!")
        

    
if __name__ == "__main__":
    solve()