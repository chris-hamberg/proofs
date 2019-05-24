def last_min(a):
    n = len(a)-1 
    location, minimum = n, a[n]
    for i in range(n-1, -1, -1):
        if a[i] < minimum:
            location, minimum = i, a[i]
    return location
