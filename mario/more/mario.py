from cs50 import get_int

h = 0
while (h <= 0 or h >= 9):
    h = get_int("Height: ")

row = h - 1
row_right = 0
for i in range(h):
    for j in range(h * 2 + 2):
        if j is h or j is (h + 1):
            print(" ", end="") 
        elif j >= h + 3 + row_right:
            continue
        elif row <= j:
            print("#", end="")
        else:
            print(" ", end="")
    row -= 1
    row_right += 1
    print()

        
        







