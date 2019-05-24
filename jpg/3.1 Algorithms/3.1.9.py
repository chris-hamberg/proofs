from math import floor

def palindrome(a):
    n = len(a) - 1
    for i in range(floor(n+1/2)):
        if a[i] != a[n-i]:
            return False
    return True
