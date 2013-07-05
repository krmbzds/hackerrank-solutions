#!/usr/bin/python3
debug = False


def displayPathtoPrincess(n, grid):

    if debug:  #debug
        for row in grid: print(row)

    for row in grid:
        if "p" in row:
            px = row.index("p")
            py = grid.index(row)

        if "m" in row:
            mx = row.index("m")
            my = grid.index(row)

    if debug:  # debug
        print(("px: {0}\tpy: {1}\nmx: {2}\tmy: {3}".format(
            px, py, mx, my)))

    while (mx != px):
        if mx > px:
            mx -= 1
            print("LEFT")
        elif mx < px:
            mx += 1
            print("RIGHT")

    while (my != py):
        if my > py:
            my -= 1
            print("UP")
        elif my < py:
            my += 1
            print("DOWN")


m = int(input())

grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
