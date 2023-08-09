from logger import logger


class NestedIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flat_list = list()
        self.create_flat_list(self.list_of_list)

    def __iter__(self):
        self.counter = -1
        return self
    
    @logger
    def __next__(self):
        self.counter += 1
        if self.counter >= len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.counter]
    
    def create_flat_list(self, input_data):
        if isinstance(input_data, list):
            for item in input_data:
                if isinstance(item, list):
                    self.create_flat_list(item)
                else:
                    self.flat_list.append(item)
        else:
            self.flat_list.append(input_data)

@logger
def nested_generator(list_of_list):
    for elem in list_of_list:
        if isinstance(elem, list):
            yield from nested_generator(elem)
        else:
            yield elem