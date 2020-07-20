def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # weight / list position for k, v in dict
    weight_dict = dict()

    i = 0
    # while i < len(weights):
    #     if weights[i] <= limit:
    #         if weight_dict[weights[i]] is not None:
    #             print("already present")
    #         else:
    #             print("adding to dict list")
    #             # weight_dict[weights[i]] = {i}
    #     i += 1
    # print(weight_dict)
    result = ()
    while i < len(weights):
        check_weight = weights[i]
        if check_weight <= limit:

            if check_weight in weight_dict and target / check_weight == 2:
                if target / weights[i] == 2:
                    result = (weight_dict[weights[i]])

            else:
                weight_dict[weights[i]] = i
        i += 1

    print(weight_dict)

    for key in weight_dict:
        target = limit - key

        print(target)
        if target in weight_dict:

            if target > key:
                result = (weight_dict[target], weight_dict[key])
            result = (int(weight_dict[key]), int(weight_dict[target]))

    return result


weights_3 = [12, 6, 7, 14, 19, 3, 0, 25, 40]


print(get_indices_of_item_weights(weights_3, 9, 7))
