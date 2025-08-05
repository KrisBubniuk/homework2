#Task 1
alice_in_wonderland = (
    "'Would you tell me, please \n"
    "Which way I ought to go from here?\n"
    "That depends a good deal on where you want to get to.'")

#Task 2
print("Кількість одинарних лапок в тексті: ", alice_in_wonderland.count("'"))
# Task 3
print()
print(alice_in_wonderland)

# Task 4
print()
black_sea_area = 436_402
azovsk_sea_area = 37_800
total_area = black_sea_area + azovsk_sea_area
print(f"Площа яку займають Чорне та Азовське моря разом становить: {total_area} км2 ")

#Task 5
print()
total_goods = 375_291
first_and_second_storage = 250_449
second_and_third_storage = 222_950

second_storage = first_and_second_storage + second_and_third_storage - total_goods
first_storage = first_and_second_storage - second_storage
third_storage = second_and_third_storage - second_storage

print(f"На першому складі: {first_storage} товарів")
print(f"На другому складі: {second_storage} товарів")
print(f"На третьому складі: {third_storage} товарів")

# Task 6
print()
months = 12 * 1.5
payment_monthly = 1179
price_total = int(months * payment_monthly)
print(f"Повна вартість компютера: {price_total}")

# Task 7
print()
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 4
e = 7128 % 5
f = 19224 % 9

print(f"Остача від ділення а): {a}")
print(f"Остача від ділення b): {b}")
print(f"Остача від ділення c): {c}")
print(f"Остача від ділення d): {d}")
print(f"Остача від ділення e): {e}")
print(f"Остача від ділення f): {f}")

# Task 8
print()
large_pizza_number = 4
large_pizza_price = 274

medium_pizza_number = 2
medium_pizza_price = 218

juice_number = 4
juice_price = 35

cake_number = 1
cake_price = 350

water_number = 3
water_price = 21

total_price = (
    large_pizza_number * large_pizza_price +
    medium_pizza_price * medium_pizza_number +
    juice_number * juice_price +
    cake_price * cake_number +
    water_price * water_number
)
print(f"{total_price} грн знадобиться для даного замовлення Іринки")

# Task 9
print()
import math
photos = 232
pages_for_photos = 8

total_pages = math.ceil(photos / pages_for_photos)
print(f"{total_pages} сторінок знадобиться Ігорю, щоб вклеїти всі фото")

# Task 10
print()
distance = 1600
liters_km = 9

total_liters = (distance / 100) * liters_km

bak_liters = 48
import math
number_stations = math.ceil(total_liters / bak_liters)
print(f"{total_liters} літрів бензину знадобиться для такої подорожі")
print(f"{number_stations} щонайменше разів родині необхідно заїхати на заправку під час цієї подорожі")