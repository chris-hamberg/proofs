def negatives(a):
    count = 0
    for i in range(len(a)):
        if a[i] < 0:
            count += 1
    return count
