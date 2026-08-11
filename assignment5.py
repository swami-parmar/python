# row = 1
# while row <= 5:
#     print("*" * row)
#     row += 1
row = 1

while row <= 4:
    # Print spaces
    space = 1
    while space <= 4 - row:
        print(" ", end="")
        space += 1

    # Print stars
    star = 1
    while star <= 2 * row - 1:
        print("*", end="")
        star += 1

    print()
    row += 1

