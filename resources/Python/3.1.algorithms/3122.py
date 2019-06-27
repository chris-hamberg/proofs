def longest_word(a):
    a += ' '
    word_length, maximum_size, maximum_index = 0, 0, 0
    for i in range(len(a)):
        if a[i] != ' ':
            word_length += 1
        else:
            index = (i - word_length)
            if word_length > maximum_size:
                maximum_size, maximum_index = word_length, index
            word_length = 0
    return maximum_index
