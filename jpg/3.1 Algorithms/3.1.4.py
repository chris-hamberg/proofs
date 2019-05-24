def max_difference(a):
    maximum = 0
    for i in range(1, len(a)):
        difference = a[i] - a[i-1]
        if difference > maximum:
            maximum = difference
    return maximum
