def largest_even(a):
    index = -1
    for i in range(len(a)):
        if not a[i] % 2:
            if (index == -1) or (a[i] > a[index]):
                index = i
    return index
