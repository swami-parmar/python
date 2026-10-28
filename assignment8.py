
# Task 1: Positional Arguments

def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(120, 3)
print("Task 1: Total Price =", result)


# Task 2: Default Arguments

def format_username(username, prefix="user_"):
    return prefix + username

print("\nTask 2: Username with Default Prefix")
print(format_username("swami"))

print("Username with Custom Prefix")
print(format_username("swami", "AI_"))


# Task 3: Movie Ticket Booking

def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie:", movie_name)
    print("Seat Type:", seat_type)
    print("Snacks:", snacks if snacks else "No snacks")
    print("--------------------")


print("\nTask 3: Movie Ticket Bookings")

# Only positional arguments
book_movie_ticket("Jawan", "Regular", "Popcorn")

# Only keyword arguments
book_movie_ticket(movie_name="Pathaan", seat_type="VIP", snacks="Nachos")

# Mix of positional and keyword arguments
book_movie_ticket("Jawan", snacks="Cold Drink", seat_type="Premium")

# Default values
book_movie_ticket("Pathaan")


# Task 4: Apply Coupon

def apply_coupon(amount, coupon_code=None):
    if coupon_code == "SAVE10":
        amount = amount - (amount * 0.10)

    return amount


print("\nTask 4: Coupon Discount")

print("Without Coupon:", apply_coupon(1000))
print("With SAVE10 Coupon:", apply_coupon(1000, "SAVE10"))
