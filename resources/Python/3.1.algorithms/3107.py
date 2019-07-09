def last_even(a):
    ''' Find the last even list entry. '''
    for i in range(len(a)-1, -1, -1):
        if not a[i] % 2:
            return i
    return None