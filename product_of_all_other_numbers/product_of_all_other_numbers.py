'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
    count = arr.count(0)
    if count > 0:
        if count == 1:
            # use arr.index to find the correct position of the product
            # the rest are zeros
            index = arr.index(0)

            # in arr, remove (the only) zero
            arr.remove(0)

            # ultiply everything thats reaining
            total = 1
            for x in arr:
                total = x * total

            # build the output array: pad beginning and the end with zeros
            # depending on index
            newarr = []
            
            # pad the beginning with zeros
            for x in arr[:index]:
                newarr.append(0)

            # add the total at the index
            newarr.append(total)

            # pad the end with zeros
            if index < len(arr) - 1:
                for x in arr[index:]:
                    newarr.append(0)

            return newarr

        else:
            return [0 for i in range(len(arr))]

    # multiply everything total
    total = 1
    for x in arr:
        total = x * total

    # iterate the list and divide total by each number
    # and use the results to create a new array
    newarr = []
    for x in arr:
        newarr.append(total / x)

    return newarr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
