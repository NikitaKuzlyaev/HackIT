import sys


def solve():
    n = int(sys.stdin.readline())

    open_cabs_queue = ['305', '309']
    visited = set()
    keys = {}

    for i in range(n):
        cab, rem = map(str, sys.stdin.readline().split("->"))
        cab = cab.strip()

        rem = list(map(str.strip, rem.split(',')))

        keys[cab] = []
        for j in rem:
            keys[cab].append(j)

    it = 0
    while it < len(open_cabs_queue):
        cab = open_cabs_queue[it]
        it += 1

        if cab == '000':
            print("YES")
            return

        if cab in visited:
            continue

        visited.add(cab)

        if cab in keys:
            for key in keys[cab]:
                open_cabs_queue.append(key)

    print("NO")
    return


if __name__ == "__main__":
    solve()
