def duplicates(a):
    ''' Find duplicate list entries. '''
    a.sort()
    positives = set()
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            positives = positives | {a[i+1]}
    return positives