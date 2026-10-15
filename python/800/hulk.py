import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    hate = "I hate"
    love = "I love"

    without_that = []
    for _ in range(n//2):
        without_that.append(hate)
        without_that.append(love)

    if n == 1:
        print("I hate it")
    elif n % 2 == 0:
        result = " that ".join(without_that)
        print(result + " it")
    else:
        without_that.append(hate)
        result = " that ".join(without_that)
        print(result + " it")


            
if __name__ == "__main__":
    solve()