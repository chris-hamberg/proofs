def insert(x, a):
    ''' 
    Insert an integer x at the correct index 
    position in a list of integers in increasing 
    order.
    '''
    a.sort()
    a.append(None)
    if a[-2] <= x:
        a[-1] = x
    else:
        i = len(a)-2
        while i+1 and (x < a[i]):
            a[i+1] = a[i]
            i -= 1
        a[i+1] = x
    return a