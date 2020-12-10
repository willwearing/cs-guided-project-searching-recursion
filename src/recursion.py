# An iterative search function 
def iter_search(arr, target):
    ''' 
    Input: array of things, target will the thing we're
    searching for 
    Output: int, the index of the element that we found 
    in the array or -1 if we didn't find it 
    ''' 
    for i, thing in enumerate(arr): # O(n)
        # base case 1: we found our thing 
        if thing == target:
            return i
    # base case 2: we traversed the entire array 
    # and we didn't find the thing
    return -1
​
# O(n) time 
# A recursive search function 
def rec_search(arr, target):
    ''' 
    Input: array of things, target will the thing we're
    searching for 
    Output: int, the index of the element that we found 
    in the array or -1 if we didn't find it 
    ''' 
    # base case 1: we traversed the entire array 
    # and we didn't find the thing
    # another we can think about this is if our 
    # input array was empty to begin with 
    if len(arr) == 0:
        return -1
    # base case 2: we find our target in the array 
    # we're going to check the last element in the 
    # array and see if it matches our target 
    if arr[-1] == target:
        return len(arr) - 1
    # what are we missing at this point? 
    # what if we aren't in one of these two situations?
    # the "iteration" step, or, how we move closer to 
    # a base case 
    arr.pop()
    return rec_search(arr, target)
​
'''
rec_search([4, 6, 5, 1, 8, 9], 100)
rec_search([4, 6, 5, 1, 8], 100)
rec_search([4, 6, 5, 1], 100)
rec_search([4, 6, 5], 100)
rec_search([4, 6], 100)
rec_search([4], 100)
rec_search([], 100) => -1 
'''
​
print("Iterative search: ", iter_search(arr, target))
print("Recursive search: ", rec_search(arr, target))