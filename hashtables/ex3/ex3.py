def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dictionaries = []
    # Your code here
    i = 0
    for array in arrays:
        new_dict = dict.fromkeys(array, "")
        dictionaries.append(new_dict)

    i = 0
    start_dict = dictionaries[0]
    duplicates = []

    while i < len(arrays):
        new_dupes = [key for key in dictionaries[i] if key in start_dict]

        duplicates = new_dupes
        i += 1

    return duplicates

    # return result
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
