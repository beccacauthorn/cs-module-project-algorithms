'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache={}):
    if n < 0:
        cache[n] = 0
        return 0
    elif n == 0:
        cache[0] = 1
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        #cache[n] = (cache[n-1] if (n-1 in cache) else eating_cookies(n-1, cache)) + \
        #           (cache[n-2] if (n-2 in cache) else eating_cookies(n-2, cache)) + \
        #           (cache[n-3] if (n-3 in cache) else eating_cookies(n-3, cache))
        return cache[n]

  

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to each {num_cookies} cookies")
