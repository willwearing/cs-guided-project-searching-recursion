def print_number_range(x, y):
    # base case
    if x > y:
        return
​
    print("inbound:", x)
    print_number_range(x+1, y)
    print("outbound:", x)
    return
    
print_number_range(2, 6)