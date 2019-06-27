def stats(x, y, z):
    a = [x, y, z]
    for i in range(0, 2):
        for j in range(0, 2):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    minimum, maximum, median, mean = a[0], a[-1], a[1], (a[0]+a[1]+a[2])/3
    return maximum, median, mean, minimum
