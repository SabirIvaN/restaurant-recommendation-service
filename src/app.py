from modules.dictionaries import type_dictionary, restaurant_dictionary;
from modules.display import display_restaurants;
from modules.sorters import quick_sort;

from database.restaurants import restaurant_data;
from database.types import types;

sorted_types = quick_sort(types)
organized_restaurants = restaurant_dictionary(restaurant_data)

def main():
    while True:
        food_type = input("What kind of food would you like?\nEnter first letter: ").strip().lower()
        try:
            type_choices = type_dictionary(sorted_types)[food_type]
        except KeyError as e:
            print(f"Sorry, {e} is not a valid input.")
        else:
            break
    print(f"Your options are ", end="")
    for i in range(len(type_choices)):
        if i < len(type_choices) - 1:
            print(type_choices[i], end=", ")
            continue
        print("and " + type_choices[i] + ".", end="\n")
    type_choice = input("Which one would you like?\nEnter name: ").strip().lower()
    while True:
        if type_choice in type_choices:
            confirmation = input(f"Would you like to view {type_choice} restaurants?\ny/n: ").strip().lower()
            break
        else:
            print("That option was not listed.")
        type_choice = input("Which one would you like?\nEnter name: ").strip().lower()
    while True:
        if confirmation == 'y':
            print(f"The {type_choice} restaurants are: ", end="\n\n")
            display_restaurants(organized_restaurants[type_choice])
            while True:
                search = input(" Would you like to continue your search?\ny/n: ").strip().lower()
                if search == 'y':
                    main()
                elif search == 'n':
                    print("Okay! Goodbye...")
                    quit()
        elif confirmation == 'n':
            print("Okay!", end="")
            while True:
                search = input(" Would you like to continue your search?\ny/n: ").strip().lower()
                if search == 'y':
                    main()
                elif search == 'n':
                    print("Okay! Goodbye...")
                    quit()
        else:
            print("That was not an option.")
            confirmation = input(f"Would you like to view {type_choice} restaurants?\ny/n: ").strip().lower()

main()
