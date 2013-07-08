#!/usr/bin/python3


def displayPathtoPrincess(n, grid):

    for row in grid:
        if "p" in row:
            px, py = row.index("p"), grid.index(row)

        if "m" in row:
            mx, my = row.index("m"), grid.index(row)

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

grid = [input().strip() for i in range(m)]

displayPathtoPrincess(m, grid)
