numRows = int(input("How many rows of Pascal's triangle?")) + 1
rows = []
for row in range(numRows):
    rows.append([])
    #newRow = []
    for col in range(row):
        if(col == 0):
            rows[row].append(1)
        elif(col == row - 1):
            rows[row].append(1)
        else:
            if(row > 0):
                rows[row].append(rows[row-1][col-1] + rows[row-1][col])
rows.pop(0)
for r in rows:
    print(r)