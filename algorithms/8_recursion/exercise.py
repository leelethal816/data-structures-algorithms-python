# 1. Write a Python program to calculate the sum of a list of numbers using recursion

def get_sum(num_list):
    if len(num_list) > 1:
        return num_list[0] + get_sum(num_list[1:])
    else:
        return num_list[0]

print(get_sum([2,3,4,5,10,12]))

# 2. Write a Python program to convert an integer to a string in any base using recursion

def toString(num, base):
    conv_string = "0123456789ABCDEF"

    if num < base:
        return conv_string[num]
    else:
        return toString(num // base, base) + conv_string[num % base]

print(toString(2835, 10))

# 3. Write a Python program to sum recursion lists using recursion.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21

def sum_recur_list(recur_list):
    total = 0

    for each in recur_list:
        if type(each) == type([]):
            total += sum_recur_list(each)
        else:
            total += each
    
    return total

print(sum_recur_list([1, 2, [3,4], [5,6]]))
