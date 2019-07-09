def last_min(a):
    ''' The last smallest integer from a list. '''
    n = len(a)-1 
    location, minimum = n, a[n]
    for i in range(n-1, -1, -1):
        if a[i] < minimum:
            location, minimum = i, a[i]
    return location
