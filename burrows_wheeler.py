def transform_bwt(data):
    transformations = []

    for i in range(len(data)):
        transformations.append(data)
        data = data[-1] + data[:-1]     # makes rotation, sort it and put it in a table
    transformations.sort()
    key = transformations.index(data)       # select the key with the index
    transformed_data = ''.join([transform[-1] for transform in transformations]) # select the data

    return transformed_data, key


def inverse_bwt(transformed_data, key):
    list3 = []
    for i in range(len(transformed_data)):
        list3.append(transformed_data[i])   # put the data into a list
        list3.sort()

    for i in range(len(transformed_data)-1):        # makes the rotation, sort it and put it in a table
        for i in range(len(transformed_data)):
            original_data = transformed_data[i] + list3[i]
            list3[i] = original_data
        list3.sort()
    original_data = list3[key]
    return original_data


# data = "banana"
# transformed_data, key = transform_bwt(data)
# original_data = inverse_bwt(transformed_data, key)
# print("Example 1:")
# print("Original Data:", data)
# print("key", key)
# print("Burrows-Wheeler Transform:", transformed_data)
# print("Inverted Data:", original_data)
# to test the program