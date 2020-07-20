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

    while i < len(weights):
        if weights[i] <= limit:
            
            print(weights[i], i)
            if weights[i] in weight_dict:
                # weight_dict[weights[i]] = weight_dict[weights[i]].append(i)
                print("item is in dict")
                weight_dict[weights[i]].append(i)
                print(weight_dict[weights[i]])
            else: 
                weight_dict[weights[i]] = [ i ]
                print("item not in dict")
        i += 1
    print(weight_dict)


    # return None

weights_3 = [4, 4]



get_indices_of_item_weights(weights_3, 2, 8)
