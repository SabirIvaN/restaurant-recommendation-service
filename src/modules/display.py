# Feature to show restaurants
def display_restaurants(list):
    for restaurant in list:
        print("\n")
        print(f"Name: { restaurant[0] }")
        print(f"Price: { restaurant[1] } / 5")
        print(f"Price: { restaurant[2] } / 5")
        print(f"Address: { restaurant[3] }")
        print("\n")
