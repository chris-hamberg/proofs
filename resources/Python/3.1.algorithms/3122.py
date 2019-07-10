def longest_word(a):
    ''' Find the longest word. '''
    a += '\u0020'
    word_length, maximum_size, maximum_index = 0, 0, 0
    for i in range(len(a)):
        if a[i] != '\u0020':
            word_length += 1
        else:
            index = (i - word_length)
            if word_length > maximum_size:
                maximum_size  = word_length
                maximum_index = index
            word_length = 0
    return maximum_index
