import os
from decorators.decorators import log_decor

PATH = os.getcwd()


@log_decor(PATH)
def flat_generator2(some_list):
    return (i for j in some_list for i in j)


if __name__ == '__main__':

    nested_list_ = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print([i for i in flat_generator2(nested_list_)])
