test = {}

def pescal(row, col) :
    index = (row , col)
    if index in test: return test(index)
    if (col == 1): return 1
    if (col == row ): return 1
    upLeft = pescal(row - 1, col - 1)
    upRight = pescal(row - 1, col)
    return upLeft + upRight

for r in range(1, 15) :
    for c in range(1, r + 1):
        print(pescal(r, c), end = "  ")
    print("")
