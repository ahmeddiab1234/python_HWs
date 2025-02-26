# HW - 3 - Recursion - Medium to Hard -  Standard Max

def max1(*iter, key=None):
    if not iter:
        raise ValueError("ValueError: max() arg is an empty sequence")
    fst, *iter = iter
    if not iter:
        return fst
    rem_max = max1(*iter, key=key)
    if key is not None:
        fst_keyed, rem_max_keyed = key(fst), key(rem_max)
        return fst if fst_keyed > rem_max_keyed else rem_max
    return fst if fst > rem_max else rem_max

def my_max(*iter, default=None, key=None):
    if not iter:
        if default is None:
            return default
        raise TypeError("TypeError: max expected 1 argument, got 0")
    if len(iter) == 1:
        if isinstance(iter[0], (list, set, tuple, str)):
            if not iter[0]: 
                if default is  None:
                    return default
                raise ValueError("ValueError: max() arg is an empty sequence")
            return max1(*iter[0], key=key)
    return max1(*iter, key=key)


if __name__ == '__main__':
    print(my_max(2, 5)) # 5
    print(my_max([10, 3, 60, 20])) # 60
    print(my_max(10, 3, 6, 20)) # 20
    print(my_max({5, 7, 1})) # 7
    print(my_max([5, 1], [4, 9])) # [5, 1]
    print(my_max('1234'))  # 4
    print(my_max('1234', '98')) # '98'
    print(my_max('1234', '98', key= len)) # '1234'
    print(my_max([5, 1], [4, 9], key= sum)) # [4, 9]

    # print(my_max())           # TypeError: max expected 1 argument, got 0
    # print(my_max(default = -1)) # TypeError: max expected 1 argument, got 0
    # print(my_max([]))         # ValueError: max() arg is an empty sequence
    print(my_max([], default = None)) # None
    # print(my_max(-15))        # TypeError: 'int' object is not iterable
    # print(my_max(3, [4]))     # TypeError: '>' not supported between instences of 'list' and 'int'