def count(s):
    total = 0
    for i in range(len(s)):
        if s[i] == '1':
            total += 1
    return total
