class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter = 0
        self.elements_counter = -1
        return self

    def __next__(self):
        self.elements_counter += 1
        if self.elements_counter >= len(self.list_of_list[self.counter]):
            self.counter += 1
            if self.counter >= len(self.list_of_list):
                raise StopIteration
            self.elements_counter = 0
        item = self.list_of_list[self.counter][self.elements_counter]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print(list(FlatIterator(list_of_lists_1)))


if __name__ == '__main__':
    test_1()
