def last_even(a):
    index = 0
    for i in range(len(a)):
        if not a[i] % 2:
            index = i
    return index
