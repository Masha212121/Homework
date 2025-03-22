cell = input()
column = ord(cell[0]) - ord('a') + 1
row = int(cell[1])
if (row + column) % 2 == 0:
    print("черная")
else:
    print("белая")