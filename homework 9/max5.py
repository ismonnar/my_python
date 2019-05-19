from random import randint

def max_sequence(p):
    """
    Функция ищет пять соседних элементов списка, сумма значений которых максимальна.
    
    >>> max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4])
    [4, 4, 4, 3, 4]
    
    >>> max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
    [7, 2, 9, 2, 9]
    """   
    prep = [p[i:i+5] for i in range(0, len(p)-4)]
    sums = list(map(sum, prep))
    indexmax = sums.index(max(sums))
    return prep[indexmax]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
