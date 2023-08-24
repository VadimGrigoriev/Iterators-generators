class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.source_list = [self.list_of_list]
        self.new_list = []
        self.counter = -1
        return self

    def __next__(self):
        while self.source_list:
            val = self.source_list.pop(-1)
            if isinstance(val, list):
                self.source_list.extend(val)
            else:
                self.new_list.append(val)
        else:

            self.counter += 1
            if self.counter >= len(self.new_list):
                raise StopIteration
            item = list(reversed(self.new_list))[self.counter]
            return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print(list(FlatIterator(list_of_lists_2)))


if __name__ == '__main__':
    test_3()
