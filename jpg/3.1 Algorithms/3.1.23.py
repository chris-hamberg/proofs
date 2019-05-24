def surjection(f, A, B):
    for b in B:
        for a in A:
            if b == f(a):
                break
        else:
            return False
    return True
