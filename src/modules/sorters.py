# Function for quick sorting
def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[-1]
    left_list = [word for word in list if word < pivot]
    right_list = [word for word in list if word > pivot]
    left_sorted = quick_sort(left_list)
    right_sorted = quick_sort(right_list)
    return left_sorted + [pivot] + right_sorted