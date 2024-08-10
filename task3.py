import types
import datetime
import os


def logger(old_function):
    def new_function(*args, **kwargs):
        func_call = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        log_str = f'время вызова {func_call} функции {old_function.__name__} параметры {args} {kwargs} результат {list(old_function(*args, **kwargs))}'
        with open('main.log', 'a') as f:
            f.writelines(log_str + '\n')
        return result

    return new_function


@logger
def flat_generator(list_of_lists):
    result = []
    for i in list_of_lists:
        result += i
    for i in result:
        yield i


def test_2():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()