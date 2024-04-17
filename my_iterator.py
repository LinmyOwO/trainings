class InfiniteSquaring:
    """Класс обеспечивает бесконечное последовательное возведение числа в квадрат"""
    def __init__(self, initial_number):
        self.number_to_square = initial_number

    def __iter__(self):
        return self

    def __next__(self):
        self.number_to_square = self.number_to_square ** 2
        return self.number_to_square