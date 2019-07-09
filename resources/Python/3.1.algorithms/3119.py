def stats(x, y, z):
    ''' Find the max, median, mean, and min. '''
    a = [x, y, z]
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    minimum, maximum = a[0], a[-1]
    median, mean = a[1], (a[0]+a[1]+a[2])/3
    return maximum, median, mean, minimum