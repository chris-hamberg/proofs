import random, math

def qsearch(term, sequence, index=0):

    endpoint = math.floor(len(sequence)/4)

    if endpoint == 0:
        if term == sequence[0]:
            return index
        elif term == sequence[1]: 
            return index +1
        else:
            return index + 2

    elif term < sequence[endpoint]:
        return qsearch(term, sequence[:endpoint], index)

    elif sequence[endpoint] <= term < sequence[endpoint*2]:
        return qsearch(term, sequence[endpoint:endpoint*2], index+endpoint)

    elif sequence[endpoint*2] <= term < sequence[endpoint*3]:
        return qsearch(term, sequence[endpoint*2:endpoint*3], index+(endpoint*2))

    elif sequence[endpoint*3] <= term:
        return qsearch(term, sequence[endpoint*3:], index+(endpoint*3))

    else:

        return False

def test(trials):

    for trial in range(trials):
        sequence = list(range(random.randrange(100, 1000)))
        term = random.choice(sequence)
        expectation = sequence.index(term)
        result = qsearch(term, sequence)
        assert expectation == result, 'expect: {expectation}\tactual: {result}'.format_map(vars())

if __name__ == '__main__':
    test(10000)
