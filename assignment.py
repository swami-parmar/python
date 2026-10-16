
fav_items = ["Kesariya", 20, 25.5, True]
print( fav_items)


fav_items[0] = "Apna Bana Le"
fav_items[1] = fav_items[1] + 1
print(fav_items)

del fav_items[2]
print( fav_items)


weekend_plan = ["Learn Python", "Play cricket", 2, "Watch a movie", 3, "Practice AI"]

removed_item = weekend_plan.pop()

print("Removed item:", removed_item)
print("Updated weekend plan:", weekend_plan)
