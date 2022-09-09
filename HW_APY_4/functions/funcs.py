from functools import reduce
import operator
from itertools import chain


# Итератор 1
class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = reduce(operator.add, nested_list)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.nested_list):
            raise StopIteration
        return self.nested_list[self.index]


# Итератор 2
def do_flat_iter1(some_list):
    return iter(reduce(operator.add, some_list))


# Итератор 3
def do_flat_iter2(some_list):
    return chain.from_iterable(some_list)


# Генератор 1
def flat_generator1(some_list):
    for i in some_list:
        for j in i:
            yield j


# Генератор 2
def flat_generator2(some_list):
    return (i for j in some_list for i in j)


# Генератор 3
def flat_generator3(some_list):
    for i in some_list:
        if isinstance(i, list):
            for j in flat_generator3(i):
                yield j
        else:
            yield i