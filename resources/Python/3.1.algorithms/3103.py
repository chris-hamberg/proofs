def sum(a):
    ''' Calculate the sum of integers in a list. '''
    total = 0
    for i in range(len(a)):
        total += a[i]
    return total