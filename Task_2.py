import types


def flat_generator(list_of_lists):
    counter = 0
    while list_of_lists:
        temporary_list = list_of_lists[counter]
        for item in temporary_list:
            yield item
        counter += 1
        if counter >= len(list_of_lists):
            return


def test_2():
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
    print(list(flat_generator(list_of_lists_1)))


if __name__ == '__main__':
    test_2()
