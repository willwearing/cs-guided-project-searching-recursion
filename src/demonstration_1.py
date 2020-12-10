"""
I was bored one day and decided to look at last names in the phonebook for my
area.
​
I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.
​
When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."
​
Example:
​
surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]
​
Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.
​
*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
def find_rotation_point(surnames):
    # Your code here
    # we don't know what the target is 
    # we know we're looking for the rotation point, 
    # but we don't know the actual name at the 
    # rotation point 
    # 1. keep track of the range during left and right
    # variables 
    left = 0
    right = len(surnames) - 1
    # 2. so long as left < right 
    while left < right:
        # 3. calculate the midpoint 
        midpoint = (left + right) // 2
        # 4. compare the midpoint element against 
        #    the first array element 
        # 5. if the midpoint element > first element 
        #    in the array 
        if surnames[midpoint] > surnames[0]:
        #    we go right, tossing out the midpoint 
        #    element itself as well 
            left = midpoint
        # 6. otherwise, we go left, but we can't 
        #    toss out the midpoint element itself,
        #    since it might be the first element 
        #    in the rotated portion of the array
        else:
            right = midpoint 
        # 7. check if left + 1 == right 
​
        if left + 1 == right:
        #    this tells us when we've narrowed the 
        #    range down to just two elements 
        #    the rotation point will be the right index 
        #    return the right index 
            return right 
​
surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]
​
print(find_rotation_point(surnames))