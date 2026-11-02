RESTAURANTS = [
    ("Mango Rice", 4.2, 25),
    ("Pad Thai House", 4.8, 40),
    ("Chicken Rice", 4.6, 15),
    ("Som Tam Corner", 4.6, 25),
    ("Boat Noodles", 4.8, 30),
]


def by_rating(r):
    return (-r[1], r[2])


def by_time(r):
    return (r[2], -r[1])


choice = input("Sort by (rating/time): ").lower()

if choice == "rating":
    result = sorted(RESTAURANTS, key=by_rating)

elif choice == "time":
    result = sorted(RESTAURANTS, key=by_time)

else:
    print("Unknown option")
    result = []

for i, restaurant in enumerate(result, start=1):
    name, rating, minutes = restaurant
    print(f"{i}. {name}, {rating} stars, {minutes} min")
