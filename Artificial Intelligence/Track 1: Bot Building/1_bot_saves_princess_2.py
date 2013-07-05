#!/usr/bin/python3
debug = False


def displayPathtoPrincess(n, grid):

    if debug: # debug
        for row in grid: print(row)

    for row in grid:
        if "p" in row:
            px, py = row.index("p"), grid.index(row)

        if "m" in row:
            mx, my = row.index("m"), grid.index(row)

    if debug: # debug
        print(("px: {0}\tpy: {1}\nmx: {2}\tmy: {3}".format(
            px, py, mx, my)))

    terminate = False

    while (mx != px):
        if mx > px:
            mx -= 1
            print("LEFT")
            terminate = True
            break
        elif mx < px:
            mx += 1
            print("RIGHT")
            terminate = True
            break

    if not terminate:
        while (my != py):
            if my > py:
                my -= 1
                print("UP")
                break
            elif my < py:
                my += 1
                print("DOWN")
                break


m = int(input())

_null = input()

grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
