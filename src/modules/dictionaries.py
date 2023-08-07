# Function to handle dictionary of types
def type_dictionary(list):
    counter = {}
    for type in list:
        if type[0] in counter.keys():
            counter[type[0]] += [type]
        else:
            counter[type[0]] = [type]
    return counter

# Function for processing a dictionary of restaurants
def restaurant_dictionary(list):
    rest_dict = {}
    for restaurant in list:
        if restaurant[0] not in rest_dict.keys():
            rest_dict[restaurant[0]] = [restaurant[1:]]
            continue
        rest_dict[restaurant[0]] += [restaurant[1:]]
    return rest_dict
