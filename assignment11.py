
# Session: Math and Random Modules

import math
import random


# Task 1: Calculate Square Roots

numbers = [16, 49, 81]

print("Task 1: Square Roots")

for number in numbers:
    print("Square root of", number, "=", math.sqrt(number))


# Task 2: Flipkart-Style Price Rounder

prices = [199.1, 349.8, 599.3]

rounded_prices = []

for price in prices:
    rounded_prices.append(math.ceil(price))

print("\nTask 2: Rounded Product Prices")
print(rounded_prices)


# Task 3: Zomato Order Bill with 10% Discount

bill_amount = 1250
discount = bill_amount * 0.10
final_bill = math.floor(bill_amount - discount)

print("\nTask 3: Zomato Bill")
print("Original Bill: Rs.", bill_amount)
print("Discount: Rs.", discount)
print("Final Bill: Rs.", final_bill)


# Task 4: Dice Roll Simulation

dice = random.randint(1, 6)

print("\nTask 4: Dice Roll")
print("You rolled:", dice)


# Task 5: Spotify-Style Random Playlist

songs = [
    "Kesariya",
    "Shape of You",
    "Believer",
    "Perfect",
    "Tum Hi Ho",
    "Brown Munde",
    "Heeriye",
    "Chaleya"
]

daily_playlist = random.sample(songs, 3)

print("\nTask 5: Today's Random Playlist")

for song in daily_playlist:
    print(song)
