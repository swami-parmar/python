
# Task 1: Round cricket scores
scores = [56.7, 102.3, 88.9, 45.2, 120.8]

rounded_scores = [round(score) for score in scores]

print("Original scores:", scores)
print("Rounded scores:", rounded_scores)


# Task 2: Sort restaurant ratings in descending order
ratings = [4.2, 3.8, 4.9, 2.5, 4.0]

sorted_ratings = sorted(ratings, reverse=True)

print("Ratings in descending order:", sorted_ratings)


# Task 3: Sort Flipkart product names alphabetically
products = ["Shoes", "Laptop", "Mobile", "Headphones", "Watch"]

products.sort()

print("Alphabetically sorted products:", products)


# Task 4: Pair restaurants with delivery times using zip()
restaurants = ["Burger Hub", "Pizza Point", "Sushi House"]
delivery_times = [30, 25, 40]

for restaurant, time in zip(restaurants, delivery_times):
    print(f"{restaurant} - {time} min")


# Task 5: Pair YouTube video titles with rounded view counts
def round_video_views(titles, views):
    return [
        (title, round(count, -3))
        for title, count in zip(titles, views)
    ]


video_titles = ["AI Tutorial", "Python Basics", "Video Editing"]
view_counts = [15450, 28760, 43210]

result = round_video_views(video_titles, view_counts)

print("Rounded video views:", result)
