
# Session: Dynamic Nested Dictionary Creation


# Task 1: Flipkart Shopping Cart

cart = {}

cart["rahul"] = {
    "item1": {"name": "Shoes", "quantity": 2, "price": 1500},
    "item2": {"name": "Watch", "quantity": 1, "price": 2500}
}

cart["priya"] = {
    "item1": {"name": "Bag", "quantity": 1, "price": 1200},
    "item2": {"name": "Headphones", "quantity": 2, "price": 2000}
}

print("Task 1: Flipkart Shopping Cart")
print(cart)


# Task 2: Spotify Dynamic Playlist

def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    playlists.setdefault(user, {})
    playlists[user].setdefault(playlist_name, [])

    song = {"title": song_title, "artist": artist}
    playlists[user][playlist_name].append(song)

    return playlists


playlists = {}

add_song_to_playlist(playlists, "rahul", "Favourites", "Kesariya", "Arijit Singh")
add_song_to_playlist(playlists, "rahul", "Favourites", "Believer", "Imagine Dragons")
add_song_to_playlist(playlists, "priya", "Chill", "Perfect", "Ed Sheeran")

print("\nTask 2: Spotify Playlists")
print(playlists)


# Task 3: IPL Match Scores

scores = {}

scores.setdefault("CSK", {})
scores["CSK"].update({
    "Ruturaj": 75,
    "Dhoni": 30,
    "Jadeja": 42
})

scores.setdefault("MI", {})
scores["MI"].update({
    "Rohit": 65,
    "Surya": 50,
    "Hardik": 25
})

print("\nTask 3: IPL Player Scores")
print(scores)

print("Ruturaj's runs:", scores["CSK"]["Ruturaj"])


# Task 4: Zomato Orders

orders = {
    101: {
        "restaurant": "Pizza House",
        "items": ["Pizza", "Garlic Bread"],
        "total": 500
    }
}


def add_order(orders, order_id, restaurant, items, total):
    orders[order_id] = {
        "restaurant": restaurant,
        "items": items,
        "total": total
    }


def update_order_total(orders, order_id, new_total):
    if order_id in orders:
        orders[order_id]["total"] = new_total
    else:
        print("Order not found")


add_order(orders, 102, "Burger Point", ["Burger", "Fries"], 300)
update_order_total(orders, 101, 550)

print("\nTask 4: Zomato Orders")
print(orders)


# Task 5: Fix KeyError in Dynamic Playlist

playlists = {
    "user1": {
        "Favourites": ["Song1", "Song2"]
    }
}

playlists.setdefault("user2", {})
playlists["user2"].setdefault("Chill", [])
playlists["user2"]["Chill"].append("Song3")

print("\nTask 5: Updated Dynamic Playlists")
print(playlists)
