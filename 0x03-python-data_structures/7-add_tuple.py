#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Take only the first two elements from each tuple or use 0 for missing values
    a = (tuple_a[0] if len(tuple_a) > 0 else 0, tuple_a[1] if len(tuple_a) > 1 else 0)
    b = (tuple_b[0] if len(tuple_b) > 0 else 0, tuple_b[1] if len(tuple_b) > 1 else 0)

    # Return a tuple with the sum of corresponding elements
    result = (a[0] + b[0], a[1] + b[1])
    return result
