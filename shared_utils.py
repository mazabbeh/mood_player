from itertools import islice


def chunkit(it, size):
    it = iter(it)

    return tuple(iter(lambda: tuple(islice(it, size)), ()))


def gimme_a_squiggly(i):
    if i % 2 == 0:
        return '{\n}'
    else:
        return '}\n{'