def print_list_of_numbers(lst):
    # base case
    if lst == []:
        return
​
    print(lst[0], lst)
    print_list_of_numbers(lst[1:])  # recursive call
​
print_list_of_numbers([0,1,2,3,4,5])