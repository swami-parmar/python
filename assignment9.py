
# Session 9: Anonymous Functions (Lambda)


# Task 1: Square of Numbers from 1 to 5

square = lambda x: x * x

print("Task 1: Squares")
for i in range(1, 6):
    print(i, "=", square(i))


# Task 2: Add 10% Service Charge Using map()

prices = [120, 250, 99, 180, 310]

updated_prices = list(map(lambda price: round(price * 1.10, 2), prices))

print("\nTask 2: Prices with 10% Service Charge")
print(updated_prices)


# Task 3: Filter Users with More Than 1000 Followers

users = [
    ("raj", 800),
    ("simran", 1500),
    ("veer", 1200),
    ("ananya", 950)
]

popular_users = list(filter(lambda user: user[1] > 1000, users))

print("\nTask 3: Users Eligible for K Badge")
for user in popular_users:
    print(user[0])


# Task 4: Sum and Product Using Lambda

calculate = lambda a, b: (a + b, a * b)

pairs = [(3, 4), (5, 2), (7, 8)]

print("\nTask 4: Sum and Product")
for a, b in pairs:
    print((a, b), "Sum and Product =", calculate(a, b))


# Task 5: Check Palindrome Using Lambda

is_palindrome = lambda text: text == text[::-1]

print("\nTask 5: Palindrome Check")
print("madam:", is_palindrome("madam"))
print("python:", is_palindrome("python"))
print("noon:", is_palindrome("noon"))
