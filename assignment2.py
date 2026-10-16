

playlist = ["Kesariya", "Apna Bana Le", "Tum Hi Ho", "Heeriye", "Ilahi"]

for i in range(len(playlist)):
    print(i + 1, playlist[i])


foods = ["Pizza", "Burger", "Dosa", "Pasta", "Fries"]

for i in range(3):
    print(foods[i])


prices = [299, 499, 150, 1200, 350]

total = 0

for price in prices:
    total = total + price

print("Total cart value:", total)



unread_counts = [2, 0, 15, 120, 5]

for count in unread_counts:
    if count > 99:
        print("99+")
    else:
        print(count)
