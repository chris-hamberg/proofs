# logical connectives
_and = lambda x, y: x and y
_or  = lambda x, y: x or y
xor = lambda x, y: x ^ y
conditional = lambda x, y: (not x) or y
biconditional = lambda x, y: _conditional(x, y) and _conditional(y, x)

# converters for internal use
_to_bool = lambda s: list(map(bool, list(map(int, list(str(s))))))
_to_bin  = lambda s: ''.join(map(str, list(map(int, s))))

# internal sequence normalization for bitwise operations
def _normalize(s1, s2):
    longer, shorter = str(max(int(s1), int(s2))), str(min(int(s1), int(s2)))
    length = len(longer) - len(shorter)
    shorter = length*'0' + shorter
    assert len(longer) == len(shorter)
    return _to_bool(longer), _to_bool(shorter)

# abstract base function for bitwise operations
def _bitwise(s1, s2, operator):
    s1, s2 = _normalize(s1, s2)
    result = []
    for v1, v2 in zip(s1, s2):
        result.append(operator(v1, v2))
    return _to_bin(result)

# bitwise public interface
band = lambda s1, s2: _bitwise(s1, s2, _and) # bitwise and
bor  = lambda s1, s2: _bitwise(s1, s2, _or)  # bitwise or
bxor = lambda s1, s2: _bitwise(s1, s2, xor)  # bitwise xor

# fuzzy connectives
fuzzy_and = lambda x, y: min(x, y)
fuzzy_or  = lambda x, y: max(x, y)

def _test():
    import random
    def gen():
        seq = ''
        for place_value in range(random.randint(1, 11)):
            seq += random.choice(['0', '1'])
        return seq
    s1, s2 = gen(), gen()
    print('sequence 1: {s1}\tsequence 2: {s2}'.format(**vars()))
    print('bitwise operation results: \nand: {0} \tor: {1}  \txor: {2}'.format(
        band(s1, s2), bor(s1, s2), bxor(s1, s2)))

if __name__ == '__main__':
    _test()
