import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    polyhedrons = []
    result = 0

    for _ in range(n):
        s = input().strip()
        polyhedrons.append(s)

    for i in polyhedrons:
        if i == "Tetrahedron":
            result += 4
        elif i == "Cube":
            result += 6
        elif i == "Octahedron":
            result += 8
        elif i == "Dodecahedron":
            result += 12
        elif i == "Icosahedron":
            result += 20

    print(result)
    
    
        
if __name__ == "__main__":
    solve()
