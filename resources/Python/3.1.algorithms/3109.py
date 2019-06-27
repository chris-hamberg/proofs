from math import floor

def palindrome(a):
    ''' Determine whether a string is a palindrome. '''
    for i in range(floor((len(a))/2)):
        if a[i] != a[(len(a)-1)-i]:
            return False
    return True