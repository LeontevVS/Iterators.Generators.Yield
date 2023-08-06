class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter_level_0 = 0
        self.counter_level_1 = -1
        self.cur_elem = list()
        return self

    def __next__(self):
        if self.counter_level_0 >= len(self.list_of_list):
            raise StopIteration
        self.cur_elem = self.list_of_list[self.counter_level_0]
        self.counter_level_1 += 1
        if self.counter_level_1 >= len(self.cur_elem):
            self.counter_level_0 += 1
            self.counter_level_1 = 0
        if self.counter_level_0 >= len(self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.counter_level_0][self.counter_level_1]


def flat_generator(list_of_lists):
    for elem in list_of_lists:
        for item in elem:
            yield item