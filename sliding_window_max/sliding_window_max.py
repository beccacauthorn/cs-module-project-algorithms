'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    maxima = []

    start_window = 0
    while start_window + k <= len(nums):
        window = nums[start_window:k + start_window]
        maxima.append(max(window))
        start_window = start_window + 1 

    return maxima


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
