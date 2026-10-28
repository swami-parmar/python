
# Task 1: Products and Prices Using zip()

products = ["Laptop", "Mobile", "Headphones"]
prices = [50000, 20000, 2000]

product_prices = dict(zip(products, prices))
print("Task 1: Product Prices")
print(product_prices)


# Task 2: Usernames and Followers Using Loop

usernames = ["rahul", "amit", "priya"]
followers = [1200, 2500, 5000]

instagram = {}

for i in range(len(usernames)):
    instagram[usernames[i]] = followers[i]

print("\nTask 2: Instagram Followers")
print(instagram)


# Task 3: IPL Teams with More Than 10 Points

teams = ["CSK", "MI", "RCB", "KKR", "SRH"]
points = [12, 8, 15, 10, 14]

team_points = dict(zip(teams, points))

print("\nTask 3: IPL Teams with More Than 10 Points")

for team, point in team_points.items():
    if point > 10:
        print(team, point)


# Task 4: Movies, Genres and Ratings Using zip()

titles = ["Pathaan", "Jawan", "3 Idiots"]
genres = ["Action", "Action", "Comedy"]
ratings = [7.5, 7.8, 8.4]

movies = []

for title, genre, rating in zip(titles, genres, ratings):
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    movies.append(movie)

print("\nTask 4: Movie Details")
print(movies)
