import numpy as np


class ProductOfNumbers:

    data_stream = []

    def __init__(self):
        self.data_stream = []

    def add(self, num: int) -> None:
        self.data_stream.append(num)

    def getProduct(self, k: int) -> int:
        nums_required = self.data_stream[len(self.data_stream) - k :]
        return np.prod(nums_required)
