def injection(f, A):
    for a in A:
        for b in A:
            if f(a) == f(b) and a != b:
                return False
    return True
