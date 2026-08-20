def get_discounted_price(price, discount_percent):
    discount = price * discount_percent / 100
    return price - discount


price = float(input("Enter price: "))
discount_percent = float(input("Enter discount percentage: "))

final_price = get_discounted_price(price, discount_percent)

print("Final price:", final_price)
