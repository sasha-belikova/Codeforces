import sys
input = sys.stdin.readline


def solve():
    n, l = map(int, input().split())    # n - amount of lanterns
                                        # l - lenght of street
    a = list(map(int, input().split())) # a - place of lantern
    a = list(set(a))
    a.sort()
    diff = []


    if len(a) > 1:
        for i in range(len(a) -1):
            current = a[i]
            next = a[i+1]
            diff.append(abs(current - next))

        if 0 in a and l in a:
            print(max(diff) / 2)
        elif 0 not in a or l not in a:
            new1 = (abs(0-a[0]))
            new2 =(abs(l - a[-1]))

            diff_new = max(diff)/2
                
            if diff_new >= max(new1, new2):
                print(diff_new)
            else:
                print(max(new1, new2))
    else:
        new1 = (abs(0-a[0]))
        new2 =(abs(l - a[-1]))
        print(max(new1, new2))


if __name__ == "__main__":
    solve()