def power2(set):
    """
    >>> power2({0,1,2,3,4})
    {8, 1, 2, 16, 4}
    """
    return {2**x for x in {0,1,2,3,4}}

if __name__ == "__main__":
    import doctest
    doctest.testmod()