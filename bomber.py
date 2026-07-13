def bomberMan(n, grid):
    if n == 1:
        return grid

    rows = len(grid)
    cols = len(grid[0])

    if n % 2 == 0:
        return ["O" * cols for _ in range(rows)]

    def explode(g):
        new = [["O"] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if g[i][j] == "O":
                    new[i][j] = "."
                    if i > 0:
                        new[i - 1][j] = "."
                    if i < rows - 1:
                        new[i + 1][j] = "."
                    if j > 0:
                        new[i][j - 1] = "."
                    if j < cols - 1:
                        new[i][j + 1] = "."

        return ["".join(row) for row in new]

    first = explode(grid)

    if n % 4 == 3:
        return first

    return explode(first)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])
    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    print(result)