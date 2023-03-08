def find_min_max(lst):
    # Initialize min and max to the first element of the list
    min_val = lst[0]
    max_val = lst[0]

    # Iterate through the list, updating min and max as needed
    for num in lst:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    # Return the min and max values
    return min_val, max_val


ls = [3, 2, 1, 5, 4, 6, 7, 8, 9, 10]
print(find_min_max(ls))s