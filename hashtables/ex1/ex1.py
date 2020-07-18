def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}

    for weight_one, weight_of_item in enumerate(weights):
        try:
            weight_two = dict[limit - weight_of_item]
        except:
            dict[weight_of_item] = weight_one
        else:
            return tuple([weight_one, weight_two])
        
    return None
