'''
Input: a List of integers
Returns: a List of integers
'''

def moving_zeroes(arr):    
    newarr = []

    # iterate over the array
    for x in arr:
        # when you see something not zero, put it a new array
        if x != 0:
            newarr.append(x)

    # fill with zeros until the correct length
    while len(newarr) != len(arr):
        newarr.append(0)

    return newarr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")