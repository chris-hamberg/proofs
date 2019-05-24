def first_max(a):
    location = 0
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            location, maximum = i, a[i]
    return location
