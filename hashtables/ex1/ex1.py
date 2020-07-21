def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = dict()
    pos = 0
    for i in weights:
        if i in weight_dict:
            weight_dict[i] = [weight_dict[i], pos]
        else:
            weight_dict[i] = pos
        pos += 1

    for key in weight_dict:
        target = limit - key

        if target in weight_dict:

            if target > 0 and limit / target == 2:
                a = weight_dict[target][1]
                b = weight_dict[target][0]

            else:
                a = weight_dict[target]
                b = weight_dict[key]
            return ([a, b])


weights_3 = [4, 4]


print(get_indices_of_item_weights(weights_3, 2, 8))
