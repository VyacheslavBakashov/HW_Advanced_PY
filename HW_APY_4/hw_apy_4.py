from functions.funcs import *
if __name__ == '__main__':

    nested_list_ = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    nested_list_2 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None, ['r', ['rr', ['rr'], ['r']]]]
    ]

    # Вызов итераторов
    some_iter = FlatIterator(nested_list_)
    print([i for i in some_iter])

    print([i for i in do_flat_iter1(nested_list_)])

    print([i for i in do_flat_iter2(nested_list_)])

    # Вызов генераторов
    print([i for i in flat_generator1(nested_list_)])

    print([i for i in flat_generator2(nested_list_)])

    print([i for i in flat_generator3(nested_list_2)])
